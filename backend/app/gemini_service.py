import io
import json
from typing import Any

import google.generativeai as genai
from PIL import Image, UnidentifiedImageError

from .config import settings


class GeminiService:
    def __init__(self) -> None:
        self._configured = False

    @property
    def configured(self) -> bool:
        return bool(settings.gemini_api_key)

    def _configure(self) -> None:
        if not settings.gemini_api_key:
            raise RuntimeError("GEMINI_API_KEY is not configured.")
        if not self._configured:
            genai.configure(api_key=settings.gemini_api_key)
            self._configured = True

    def analyze_image(self, image_bytes: bytes, reference_text: str | None) -> dict[str, Any]:
        self._configure()

        try:
            image = Image.open(io.BytesIO(image_bytes))
        except UnidentifiedImageError as exc:
            raise ValueError("Unable to parse image bytes.") from exc

        prompt = (
            "Analyze this image carefully and return valid JSON only with keys: "
            "title, description, key_objects, scene_context, relation_to_reference, "
            "confidence, and notes. "
            "The relation_to_reference field must explain how the image aligns with or "
            "differs from the given reference text. "
            f"Reference text: {reference_text or 'No reference provided.'}"
        )

        model = genai.GenerativeModel(settings.gemini_model)
        response = model.generate_content(
            [prompt, image],
            generation_config={
                "temperature": 0.2,
                "response_mime_type": "application/json",
            },
        )

        raw = (response.text or "").strip()
        if not raw:
            return {
                "title": "No response",
                "description": "Gemini did not return content.",
                "key_objects": [],
                "scene_context": "",
                "relation_to_reference": "Unknown",
                "confidence": "low",
                "notes": "",
            }

        try:
            payload = json.loads(raw)
            if isinstance(payload, dict):
                return payload
        except json.JSONDecodeError:
            pass

        return {
            "title": "Unstructured response",
            "description": raw,
            "key_objects": [],
            "scene_context": "",
            "relation_to_reference": "Could not parse JSON.",
            "confidence": "unknown",
            "notes": "Returned raw text because response was not valid JSON.",
        }


gemini_service = GeminiService()
