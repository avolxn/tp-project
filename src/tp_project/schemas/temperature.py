from pydantic import BaseModel, Field


class TemperatureConvertRequest(BaseModel):
    temperature: float = Field(..., description="Температура для конвертации")
    from_unit: str = Field(..., description="Единица измерения температуры для конвертации из")
    to_unit: str = Field(..., description="Единица измерения температуры для конвертации в")


class TemperatureConvertResponse(BaseModel):
    temperature: float = Field(..., description="Температура для конвертации")
    from_unit: str = Field(..., description="Единица измерения температуры для конвертации из")
    to_unit: str = Field(..., description="Единица измерения температуры для конвертации в")
    result: float = Field(..., description="Температура после конвертации")
