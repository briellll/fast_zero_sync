from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import encode
from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()

SECRET_KEY = 'your-secret-key'  # provisório
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_passwords: str):
    return pwd_context.verify(plain_password, hashed_passwords)


def create_access_token(data: dict):
    to_encode = data.copy()

    # adiciona um tempo de 30 minutos para expiração
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({'exp': expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
