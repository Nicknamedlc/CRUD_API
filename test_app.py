from http import HTTPStatus

from starlette.testclient import TestClient

import app


def test_root():
    client = TestClient(app.app)
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}


def test_say_hello():
    client = TestClient(app.app)
    response = client.get('/olamundo')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
