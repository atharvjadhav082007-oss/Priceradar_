import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "priceradar"
    DEBUG: bool = True
    SECRET_KEY: str = "your-secret-key"
    ALLOWED_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"

settings = Settings()
