from fastapi import APIRouter

from tp_project.api.currency import router as currency_router
from tp_project.api.temperature import router as temperature_router

router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    return {
        "title": "Currency and Temperature Converter",
        "description": "API for Currency and Temperature Converter",
        "version": "0.1.0",
        "docs_url": "/docs",
    }


router.include_router(currency_router, prefix="/currency")
router.include_router(temperature_router, prefix="/temperature")
