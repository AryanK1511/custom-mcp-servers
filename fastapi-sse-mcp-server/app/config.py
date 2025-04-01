from pydantic_settings import BaseSettings

from app.constants import PROJECT_NAME


class Settings(BaseSettings):
    PROJECT_NAME: str = PROJECT_NAME
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
