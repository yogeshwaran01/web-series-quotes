from fastapi.testclient import TestClient
from api.main import app
from api.routes.quote import get_by_id

from data import data

client = TestClient(app)


def test_api():
    response = client.get("/quote")
    assert response.status_code == 200
    response = client.get("/quote?series=dark&id=2")
    assert response.json() == get_by_id(data["dark"], 2)


def test_image():
    response = client.get("/pic/solid")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/jpeg"
