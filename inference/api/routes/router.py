from fastapi import APIRouter

from inference.api.routes import health_check, prediction

api_router = APIRouter()
api_router.include_router(health_check.router, tags=["health"], prefix="/health")
api_router.include_router(prediction.router, tags=["prediction"], prefix="/v1")
