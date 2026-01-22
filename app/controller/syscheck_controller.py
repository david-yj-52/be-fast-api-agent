from pathlib import Path

from fastapi import APIRouter

from app.config.config_manager import ConfigManager

router = APIRouter(
    prefix="/check",
    tags=["health"],
)

settings = ConfigManager()

@router.get("/health/")
async def get_agent_health_status():
    return {
        "status": "active",
        "version": settings.AP_VERSION,
        "path": Path(__file__).resolve()
    }