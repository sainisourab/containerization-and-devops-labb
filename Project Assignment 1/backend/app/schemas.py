from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, HttpUrl, model_validator


class AnalyzeRequest(BaseModel):
    image_url: HttpUrl | None = None
    image_base64: str | None = None
    reference_text: str | None = None

    @model_validator(mode="after")
    def validate_source(self) -> "AnalyzeRequest":
        if not self.image_url and not self.image_base64:
            raise ValueError("Provide either image_url or image_base64.")
        return self


class RecordResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    input_source: str
    image_url: str | None
    reference_text: str | None
    analysis: dict[str, Any]
    created_at: datetime


class HealthResponse(BaseModel):
    status: str
    db_status: str
    gemini_configured: bool
