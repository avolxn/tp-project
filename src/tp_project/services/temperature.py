class TemperatureConverterService:
    def convert(self, temperature: float, from_unit: str, to_unit: str) -> float:
        """Конвертирует температуру из одной единицы измерения в другую

        Args:
            temperature (float): Температура для конвертации
            from_unit (str): Единица измерения температуры для конвертации из
            to_unit (str): Единица измерения температуры для конвертации в

        Raises:
            ValueError: Некорректная единица измерения температуры

        Returns:
            float: Температура после конвертации
        """
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()

        if from_unit == "C":
            celcius = temperature
        elif from_unit == "F":
            celcius = (temperature - 32) * 5 / 9
        elif from_unit == "K":
            celcius = temperature - 273.15
        else:
            raise ValueError(f"Некорректная единица измерения температуры: {from_unit}")

        if to_unit == "C":
            return celcius
        elif to_unit == "F":
            return (celcius * 9 / 5) + 32
        elif to_unit == "K":
            return celcius + 273.15
        else:
            raise ValueError(f"Некорректная единица измерения температуры: {to_unit}")


temperature_converter_service = TemperatureConverterService()
