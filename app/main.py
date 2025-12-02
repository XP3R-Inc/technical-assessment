"""FastAPI entrypoint."""

from __future__ import annotations

from fastapi import FastAPI

from app.api.routes import api_router
from app.core.config import get_settings
from app.db.session import Base, engine

# Import models so that metadata is registered before running migrations.
from app.models import customer as customer_model  # noqa: F401
from app.models import opportunity as opportunity_model  # noqa: F401


def create_app() -> FastAPI:
    """Application factory used by ASGI servers."""
    settings = get_settings()
    app = FastAPI(title=settings.app_name)

    @app.on_event("startup")
    def startup() -> None:
        """Initialize database metadata."""
        Base.metadata.create_all(bind=engine)

    app.include_router(api_router, prefix="/api")
    return app


app = create_app()


