"""
Application Configuration Settings
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    APP_NAME: str = "MeishiBridge API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    DATABASE_URL: Optional[str] = None

    SECRET_KEY: str = "dev-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080

    FRONTEND_URL: str = "http://localhost:3000"

    SUPABASE_URL: Optional[str] = None
    SUPABASE_KEY: Optional[str] = None

    class Config:
        env_file = ".env.local"
        case_sensitive = True


settings = Settings()
