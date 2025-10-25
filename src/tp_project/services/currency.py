import requests

from tp_project.core import settings


class ExchangeRateAPIClient:
    def __init__(self):
        self.api_key = settings.CURRENCY_API_KEY
        self.base_url = settings.CURRENCY_BASE_URL

    def get_exchange_rates(self, from_currency: str) -> dict[str, float]:
        """Получает курсы валют от API

        Args:
            from_currency (str): Код валюты для конвертации из

        Raises:
            ValueError: Некорректный код валюты

        Returns:
            dict[str, float]: Курсы валют
        """
        url = f"{self.base_url}/{self.api_key}/latest/{from_currency}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["result"] == "error":
            raise ValueError(f"Некорректный код валюты: {from_currency}")

        return data["conversion_rates"]


class CurrencyConverterService:
    def __init__(self):
        self.exchange_rate_api_client = ExchangeRateAPIClient()

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Конвертирует сумму из одной валюты в другую

        Args:
            amount (float): Сумма для конвертации
            from_currency (str): Код валюты для конвертации из
            to_currency (str): Код валюты для конвертации в

        Raises:
            ValueError: Некорректный код валюты

        Returns:
            float: Сумма после конвертации
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        exchange_rates = self.exchange_rate_api_client.get_exchange_rates(from_currency)

        if to_currency not in exchange_rates:
            raise ValueError(f"Некорректный код валюты: {to_currency}")

        return amount * exchange_rates[to_currency]


currency_converter_service = CurrencyConverterService()
