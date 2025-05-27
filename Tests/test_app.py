from http import HTTPStatus


def test_root(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}


def test_say_hello(client):
    response = client.get('/olamundo')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'user@example.com',
        'username': 'string',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'string', 'email': 'user@example.com', 'id': 1}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'texto',
            'email': 'texto@example.com',
            'password': 'texto',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'texto',
        'email': 'texto@example.com',
        'id': 1,
    }
    response = client.put(
        '/users/0',
        json={
            'username': 'texto',
            'email': 'texto@email.com',
            'password': 'texto',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_read_user_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'texto',
        'email': 'texto@example.com',
        'id': 1,
    }
    response = client.get('/users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'texto',
        'email': 'texto@example.com',
        'id': 1,
    }
    response = client.delete('/users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
