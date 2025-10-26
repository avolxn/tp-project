from pydantic import BaseModel, Field


class TemperatureConvertResponse(BaseModel):
    temperature: float = Field(..., description="Температура для конвертации")
    from_unit: str = Field(..., description="Единица измерения температуры для конвертации из (C, F, K)")
    to_unit: str = Field(..., description="Единица измерения температуры для конвертации в (C, K, F)")
    result: float = Field(..., description="Температура после конвертации")
