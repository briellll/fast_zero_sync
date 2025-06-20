from sqlalchemy import create_engine, select

from fast_zero.models import User


def test_create_user(session):
    user = User(
            username='gabriel', email='gabriel@gmail.com', password='senha123'
    )

    session.add(user)
    session.commit()

    result = session.scalar(
            select(User).where(User.email == 'gabriel@gmail.com')
    )

    assert result.username == 'gabriel' # type:ignore

