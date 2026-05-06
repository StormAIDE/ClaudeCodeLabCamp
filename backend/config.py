"""
Application configuration using Pydantic settings.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import List, Union


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    APP_NAME: str = "Tech News Aggregator"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # CORS
    CORS_ORIGINS: Union[List[str], str] = "http://localhost:5173,http://localhost:3000"

    # Anthropic direct API (fallback when no AWS credentials)
    ANTHROPIC_API_KEY: str = ""

    # AWS / Bedrock credentials (takes priority if set)
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_SESSION_TOKEN: str = ""
    AWS_DEFAULT_REGION: str = "eu-west-1"

    # Model ID — use Bedrock ARN when on AWS, plain model name for Anthropic API
    CLAUDE_MODEL_ID: str = "claude-sonnet-4-6"

    # News API Configuration
    NEWS_API_KEY: str = ""  # Optional: Set via environment for real news API
    DATABASE_PATH: str = "./data/articles.db"

    @property
    def use_bedrock(self) -> bool:
        """True when AWS credentials are present — use Strands SDK + Bedrock."""
        return bool(self.AWS_ACCESS_KEY_ID and self.AWS_SECRET_ACCESS_KEY)

    @field_validator('CORS_ORIGINS', mode='before')
    @classmethod
    def parse_cors_origins(cls, v):
        """Parse CORS_ORIGINS from comma-separated string or list."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(',')]
        return v

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        env_ignore_empty=True,
    )


settings = Settings()
