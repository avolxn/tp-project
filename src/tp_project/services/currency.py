import httpx

from tp_project.core.config import get_settings
from tp_project.services.cache import get_cache_service


class ExchangeRateAPIClient:
    async def get_exchange_rates(self, from_currency: str) -> dict[str, float]:
        """Получает курсы валют от API с кэшированием в Redis

        Args:
            from_currency (str): Код валюты для конвертации из

        Raises:
            ValueError: Некорректный код валюты

        Returns:
            dict[str, float]: Курсы валют
        """
        cache_key = f"exchange_rates:{from_currency}"
        cache = get_cache_service()
        settings = get_settings()

        cached = await cache.get(cache_key)
        if cached:
            return cached

        url = f"{settings.CURRENCY_BASE_URL}/{settings.CURRENCY_API_KEY}/latest/{from_currency}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)
            data = response.json()

        if data["result"] == "error":
            raise ValueError(f"Некорректный код валюты: {from_currency}")

        rates = data["conversion_rates"]

        await cache.set(cache_key, rates)

        return rates


class CurrencyConverterService:
    def __init__(self):
        self.exchange_rate_api_client = ExchangeRateAPIClient()

    async def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
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

        exchange_rates = await self.exchange_rate_api_client.get_exchange_rates(from_currency)

        if to_currency not in exchange_rates:
            raise ValueError(f"Некорректный код валюты: {to_currency}")

        return amount * exchange_rates[to_currency]


_currency_converter_service: CurrencyConverterService | None = None


def get_currency_converter_service() -> CurrencyConverterService:
    global _currency_converter_service
    if _currency_converter_service is None:
        _currency_converter_service = CurrencyConverterService()
    return _currency_converter_service
