from http import HTTPStatus


def test_get_token(client, user, token):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_wrong_email(client, user, token):
    response = client.post(
        '/auth/token',
        data={
            'username': user.email + 'corcovado',
            'password': user.clean_password,
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_wrong_password(client, user, token):
    response = client.post(
        '/auth/token',
        data={
            'username': user.email,
            'password': user.clean_password + 'corcovado',
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}
