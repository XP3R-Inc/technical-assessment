"""Application configuration utilities."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def _load_env_file() -> None:
    """Load environment variables from the file pointed to by ENV_FILE."""
    env_file = os.environ.get("ENV_FILE", ".env")
    env_path = Path(env_file)
    if env_path.is_file():
        load_dotenv(env_path)


_load_env_file()


class Settings(BaseSettings):
    """Application settings sourced from environment variables."""

    model_config = SettingsConfigDict(env_file=None, extra="ignore")

    app_name: str = Field(default="Technical Assessment API")
    environment: str = Field(default="local")

    mysql_host: str = Field(validation_alias="MYSQL_HOST")
    mysql_port: int = Field(default=3306, validation_alias="MYSQL_PORT")
    mysql_user: str = Field(validation_alias="MYSQL_USER")
    mysql_password: str = Field(validation_alias="MYSQL_PASSWORD")
    mysql_db: str = Field(validation_alias="MYSQL_DB")
    echo_sql: bool = Field(default=False, validation_alias="ECHO_SQL")

    @property
    def database_url(self) -> str:
        """Construct a SQLAlchemy-compatible MySQL connection string."""
        return (
            "mysql+pymysql://"
            f"{self.mysql_user}:{self.mysql_password}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_db}"
            "?charset=utf8mb4"
        )


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()


