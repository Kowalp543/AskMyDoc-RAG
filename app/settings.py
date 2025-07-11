from pydantic_settings import BaseSettings
from pydantic import Field
import os


class Settings(BaseSettings):
    app_name: str = "AskMyDoc-RAG"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000

    database_url: str = Field(..., alias="DATABASE_URL")
    openai_api_key: str | None = Field(None, alias="OPENAI_API_KEY")

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        env_file_encoding = "utf-8"


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
