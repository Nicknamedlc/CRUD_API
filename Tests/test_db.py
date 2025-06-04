from dataclasses import asdict

import pytest
from sqlalchemy import select

from src.models import User


@pytest.mark.asyncio
async def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='test', email='teste@teste.com', password='secret'
        )

        session.add(new_user)
        await session.commit()

    user = await session.scalar(select(User).where(User.username == 'test'))

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'teste@teste.com',
        'password': 'secret',
        'created_at': time,
        'updated_at': time,
    }


# def test_create_task(session, user):
#     task = Task(
#         title='Test Task',
#         description='Vasco',
#         state='criada',
#         user_id=user.id,
#     )
#     session.add(task)
#     session.commit()
#
#     task = session.scalar(select(task))
#
#     assert asdict(task) == {
#         'description': 'Vasco',
#         'id': 1,
#         'state': 'criada',
#         'title': 'Test Task',
#         'user_id': 1,
#     }


# def test_create_task(session, user):
#     task = Task(
#         title='Test Task',
#         description='Vasco',
#         state='criada',
#         user_id=user.id,
#     )
#     session.add(task)
#     session.commit()
#
#     task = session.scalar(select(task))
#
#     assert asdict(task) == {
#         'description': 'Vasco',
#         'id': 1,
#         'state': 'criada',
#         'title': 'Test Task',
#         'user_id': 1,
#     }
