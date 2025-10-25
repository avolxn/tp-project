from fastapi import APIRouter

from tp_project.api.currency import router as currency_router
from tp_project.api.temperature import router as temperature_router

router = APIRouter()


router.include_router(currency_router, prefix="/currency")
router.include_router(temperature_router, prefix="/temperature")
