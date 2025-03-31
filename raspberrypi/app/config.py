# raspberrypi/app/config.py

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    RASPBERRYPI_IP: str
    RASPBERRYPI_USERNAME: str
    RASPBERRYPI_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()
