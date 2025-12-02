"""Aggregate API routers."""

from fastapi import APIRouter

from app.api import customers, opportunities

api_router = APIRouter()
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(
    opportunities.router, prefix="/opportunities", tags=["opportunities"]
)


