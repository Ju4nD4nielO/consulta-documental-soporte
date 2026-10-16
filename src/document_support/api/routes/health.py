"""Operational health endpoints."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    """Stable contract returned by the liveness endpoint."""

    status: Literal["ok"]


@router.get("/health", response_model=HealthResponse, summary="Check API liveness")
async def health_check() -> HealthResponse:
    """Report whether the API process can accept requests."""

    return HealthResponse(status="ok")
