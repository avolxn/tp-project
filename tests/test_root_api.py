from fastapi.testclient import TestClient

from tp_project.app import app

client = TestClient(app)


def test_root_endpoint():
    """Тест корневого endpoint"""
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Currency and Temperature Converter"
    assert data["version"] == "0.1.0"
