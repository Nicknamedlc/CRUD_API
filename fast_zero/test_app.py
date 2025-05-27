from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app


class TestApp:
    import pytest
    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_root(self, client):
        response = client.get("/")
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"message": "Olá Mundo"}

    def test_say_hello(self, client):
        response = client.get("/olamundo")
        assert response.status_code == HTTPStatus.OK
        assert '<h1> Olá Mundo </h1>' in response.text

    def test_create_user(self, client):
        response = client.post("/users", json={
            "username": "string",
            "email": "user@example.com",
            "password": "string"
        })
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == {
            "id": 1,
            "email": "user@example.com",
            "username": "string",
        }

    def test_read_users(self, client):
        response = client.get("/users/")
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {

            'users': [
                {
                    'username': 'string',
                    'email': 'user@example.com',
                    'id': 1
                }
            ]
        }
