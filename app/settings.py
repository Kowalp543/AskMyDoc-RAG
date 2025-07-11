from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AskMyDoc-RAG"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000

    database_url: str

    openai_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
