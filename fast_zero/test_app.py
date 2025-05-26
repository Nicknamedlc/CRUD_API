from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


class TestApp:
    def test_root(self):
        response = client.get("/")
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"message": "Olá Mundo"}

    def test_say_hello(self):
        response = client.get("/olamundo")
        assert response.status_code == HTTPStatus.OK
        assert '<h1> Olá Mundo </h1>' in response.text
    def test_create_user(self):
        response = client.post("/users", json={"name": ""})
        assert response.status_code == HTTPStatus.CREATED