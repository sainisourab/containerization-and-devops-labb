from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str
    gemini_api_key: str
    gemini_model: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


def _get_env(key: str, default: str = "") -> str:
    return os.getenv(key, default).strip()


def load_settings() -> Settings:
    return Settings(
        postgres_host=_get_env("POSTGRES_HOST", "database"),
        postgres_port=int(_get_env("POSTGRES_PORT", "5432")),
        postgres_db=_get_env("POSTGRES_DB", "image_analyzer"),
        postgres_user=_get_env("POSTGRES_USER", "image_user"),
        postgres_password=_get_env("POSTGRES_PASSWORD", "change_me"),
        gemini_api_key=_get_env("GEMINI_API_KEY", ""),
        gemini_model=_get_env("GEMINI_MODEL", "gemini-1.5-flash"),
    )


settings = load_settings()
