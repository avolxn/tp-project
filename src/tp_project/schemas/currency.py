from pydantic import BaseModel, Field


class CurrencyConvertResponse(BaseModel):
    amount: float = Field(..., description="Сумма валюты для конвертации")
    from_currency: str = Field(..., description="Код валюты для конвертации из")
    to_currency: str = Field(..., description="Код валюты для конвертации в")
    result: float = Field(..., description="Сумма валюты после конвертации")
