from fastapi.testclient import TestClient
from quoteGenerator.main import app

client = TestClient(app)

def test_generate_quote():
    response = client.get("/generate?theme=success")
    assert response.status_code == 200
    json_data = response.json()
    assert "quote" in json_data
    assert isinstance(json_data["quote"], str)
    assert len(json_data["quote"]) > 0

def test_history():
    # Call /generate first to make sure something is stored
    client.get("/generate?theme=test")

    response = client.get("/history")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, list)
    assert len(json_data) >= 1  # At least one quote must exist
    assert "quote" in json_data[0]
    assert "timestamp" in json_data[0]
