from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password_hash(plain_password: str, hashed_passwords: str):
    return pwd_context.verify(plain_password, hashed_passwords)
