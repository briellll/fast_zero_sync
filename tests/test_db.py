from sqlalchemy import create_engine

from fast_zero.models import User


def test_create_user():
    engine = create_engine(
        'sqlite:////database.db'
    )
    user = User(
        username='gabriel', email='gabriel@gmail.com', password='senha123'
    )

    assert user.username == 'gabriel'
