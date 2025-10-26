from fastapi import APIRouter, HTTPException, Query

from tp_project.schemas import CurrencyConvertResponse
from tp_project.services import currency_converter_service

router = APIRouter(tags=["currency"])


@router.get("/convert", response_model=CurrencyConvertResponse)
async def convert_currency(
    amount: float = Query(..., description="Сумма валюты для конвертации"),
    from_currency: str = Query(..., description="Код валюты для конвертации из"),
    to_currency: str = Query(..., description="Код валюты для конвертации в"),
):
    """Конвертирует валюту из одной в другую используя актуальные курсы"""
    try:
        result = currency_converter_service.convert(
            amount=amount,
            from_currency=from_currency,
            to_currency=to_currency,
        )

        return CurrencyConvertResponse(
            amount=amount,
            from_currency=from_currency.upper(),
            to_currency=to_currency.upper(),
            result=round(result, 2),
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при конвертации: {str(e)}") from e
