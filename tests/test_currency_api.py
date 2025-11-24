from unittest.mock import patch

from fastapi.testclient import TestClient

from tp_project.app import app

client = TestClient(app)


@patch("tp_project.services.currency.ExchangeRateAPIClient.get_exchange_rates")
def test_currency_convert_success(mock_get_rates):
    """Тест успешной конвертации валюты"""
    mock_get_rates.return_value = {"USD": 1.0, "EUR": 0.85, "RUB": 75.0}

    response = client.get("/currency/convert?amount=100&from_currency=USD&to_currency=EUR")
    assert response.status_code == 200

    data = response.json()
    assert data["amount"] == 100.0
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "EUR"
    assert data["result"] == 85.0


@patch("tp_project.services.currency.ExchangeRateAPIClient.get_exchange_rates")
def test_currency_convert_invalid_from_currency(mock_get_rates):
    """Тест с некорректной валютой 'from'"""
    mock_get_rates.side_effect = ValueError("Некорректный код валюты: XXX")

    response = client.get("/currency/convert?amount=100&from_currency=XXX&to_currency=EUR")
    assert response.status_code == 400


@patch("tp_project.services.currency.ExchangeRateAPIClient.get_exchange_rates")
def test_currency_convert_invalid_to_currency(mock_get_rates):
    """Тест с некорректной валютой 'to'"""
    mock_get_rates.return_value = {"USD": 1.0, "EUR": 0.85}

    response = client.get("/currency/convert?amount=100&from_currency=USD&to_currency=XXX")
    assert response.status_code == 400


def test_currency_convert_missing_params():
    """Тест API с отсутствующими параметрами"""
    response = client.get("/currency/convert?amount=100")
    assert response.status_code == 422
