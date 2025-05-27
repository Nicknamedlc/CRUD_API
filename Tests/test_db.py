from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='test', email='teste@teste.com', password='secret'
    )

    session.add(new_user)
    session.commit()

    session.scalar(select(User).where(User.username == 'test'))

    assert asdict(User) == {
        'id': 1,
        'username': 'test',
        'email': 'teste@teste.com',
        'password': 'secret',
        # 'created_at':
    }
