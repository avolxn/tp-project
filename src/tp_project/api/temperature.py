from fastapi import APIRouter, HTTPException, Query

from tp_project.schemas import TemperatureConvertResponse
from tp_project.services import temperature_converter_service

router = APIRouter(tags=["temperature"])


@router.get("/convert", response_model=TemperatureConvertResponse)
async def convert_temperature(
    temperature: float = Query(..., description="Температура для конвертации"),
    from_unit: str = Query(..., description="Единица измерения температуры для конвертации из (C, F, K)"),
    to_unit: str = Query(..., description="Единица измерения температуры для конвертации в (C, F, K)"),
):
    """Конвертирует температуру между единицами измерения (C, F, K)"""
    try:
        result = temperature_converter_service.convert(
            temperature=temperature,
            from_unit=from_unit,
            to_unit=to_unit,
        )

        return TemperatureConvertResponse(
            temperature=temperature,
            from_unit=from_unit.upper(),
            to_unit=to_unit.upper(),
            result=round(result, 2),
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при конвертации: {str(e)}") from e
