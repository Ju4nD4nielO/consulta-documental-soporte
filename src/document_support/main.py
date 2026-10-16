"""FastAPI application factory and ASGI entry point."""

from fastapi import FastAPI

from document_support.api.router import api_router
from document_support.config import get_settings


def create_app() -> FastAPI:
    """Build the application without hidden module-level configuration."""

    settings = get_settings()
    application = FastAPI(
        title=settings.name,
        version="0.1.0",
        description="API for grounded question answering over private documents.",
    )
    application.include_router(api_router, prefix="/api/v1")
    return application


app = create_app()
