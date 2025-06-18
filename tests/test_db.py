from fast_zero.models import User


def test_create_user():
    user = User(
        username='gabriel', email='gabriel@gmail.com', password='senha123'
    )

    assert user.username == 'dunossauro'
