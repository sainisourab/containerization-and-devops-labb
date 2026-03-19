import asyncio
import base64
import binascii
import re
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from .database import db
from .gemini_service import gemini_service
from .schemas import AnalyzeRequest, HealthResponse, RecordResponse

DATA_URL_PATTERN = re.compile(r"^data:(?P<mime>[\w/+.-]+);base64,(?P<data>.+)$", re.DOTALL)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await db.connect()
    try:
        yield
    finally:
        await db.disconnect()


app = FastAPI(
    title="Gemini Image Analyzer API",
    description="Analyze images with Gemini and persist results in PostgreSQL.",
    version="1.0.0",
    lifespan=lifespan,
)

# Enables browser frontend calls from LAN origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def _extract_image(request: AnalyzeRequest) -> tuple[bytes, str, str | None]:
    if request.image_url:
        async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as client:
            response = await client.get(str(request.image_url))

        if response.status_code >= 400:
            raise HTTPException(
                status_code=400,
                detail=f"Could not fetch image URL. HTTP {response.status_code}.",
            )

        content_type = response.headers.get("content-type", "")
        if "image" not in content_type.lower():
            raise HTTPException(status_code=400, detail="Provided URL is not an image.")

        return response.content, "url", str(request.image_url)

    encoded = (request.image_base64 or "").strip()
    match = DATA_URL_PATTERN.match(encoded)
    if match:
        encoded = match.group("data")

    try:
        image_bytes = base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise HTTPException(status_code=400, detail="Invalid base64 image data.") from exc

    if not image_bytes:
        raise HTTPException(status_code=400, detail="Decoded image is empty.")

    return image_bytes, "base64", None


@app.get("/health", response_model=HealthResponse)
async def healthcheck() -> HealthResponse:
    try:
        db_ok = await db.ping()
        db_status = "healthy" if db_ok else "unhealthy"
    except Exception:
        db_status = "unhealthy"

    status = "ok" if db_status == "healthy" else "degraded"
    return HealthResponse(
        status=status,
        db_status=db_status,
        gemini_configured=gemini_service.configured,
    )


@app.post("/records", response_model=RecordResponse, status_code=201)
async def create_record(request: AnalyzeRequest) -> RecordResponse:
    image_bytes, input_source, image_url = await _extract_image(request)

    try:
        analysis = await asyncio.to_thread(
            gemini_service.analyze_image,
            image_bytes,
            request.reference_text,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Gemini request failed: {exc}") from exc

    record = await db.insert_record(
        input_source=input_source,
        image_url=image_url,
        reference_text=request.reference_text,
        analysis=analysis,
    )
    return RecordResponse(**record)


@app.get("/records", response_model=list[RecordResponse])
async def get_records(limit: int = Query(default=50, ge=1, le=200)) -> list[RecordResponse]:
    rows = await db.list_records(limit=limit)
    return [RecordResponse(**row) for row in rows]
