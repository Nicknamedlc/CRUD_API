from dataclasses import asdict

from sqlalchemy import select

from src.models import Task, User


def test_create_user(session, mock_db_time, user):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='test', email='teste@teste.com', password='secret'
        )

        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'test'))

    assert asdict(user) == {
        'id': 2,
        'username': 'test',
        'email': 'teste@teste.com',
        'password': 'secret',
        'created_at': time,
        'updated_at': time,
        'tasks': [],
    }


def test_create_task(session, user):
    task = Task(
        title='Test Task',
        description='Vasco',
        state='criada',
        user_id=user.id,
    )
    session.add(task)
    session.commit()

    task = session.scalar(select(task))

    assert asdict(task) == {
        'description': 'Vasco',
        'id': 1,
        'state': 'criada',
        'title': 'Test Todo',
        'user_id': 1,
    }
