from fastapi.testclient import TestClient

from tp_project.app import app

client = TestClient(app)


def test_temperature_convert_celsius_to_fahrenheit():
    """Тест API конвертации температуры из Цельсия в Фаренгейт"""
    response = client.get("/temperature/convert?temperature=0&from_unit=C&to_unit=F")
    assert response.status_code == 200

    data = response.json()
    assert data["temperature"] == 0.0
    assert data["from_unit"] == "C"
    assert data["to_unit"] == "F"
    assert data["result"] == 32.0


def test_temperature_convert_fahrenheit_to_celsius():
    """Тест API конвертации температуры из Фаренгейта в Цельсий"""
    response = client.get("/temperature/convert?temperature=32&from_unit=F&to_unit=C")
    assert response.status_code == 200

    data = response.json()
    assert data["temperature"] == 32.0
    assert data["from_unit"] == "F"
    assert data["to_unit"] == "C"
    assert data["result"] == 0.0


def test_temperature_convert_invalid_unit():
    """Тест API с некорректной единицей измерения"""
    response = client.get("/temperature/convert?temperature=25&from_unit=X&to_unit=C")
    assert response.status_code == 400


def test_temperature_convert_missing_params():
    """Тест API с отсутствующими параметрами"""
    response = client.get("/temperature/convert?temperature=25")
    assert response.status_code == 422
