from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_home():
    response = client.get("/")
    assert response.status_code == 200
def test_predict_positive():
    response = client.post("/predict", json={"text": "This is excellent service"})
    assert response.status_code == 200
