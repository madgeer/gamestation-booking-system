# Load .env (DB URL, Secret Key)
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "GameStation API"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()