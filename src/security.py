from pwdlib import PasswordHash

pdw_context = PasswordHash.recommended()


def get_password_hash(password: str):
    return pdw_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pdw_context.verify(plain_password, hashed_password)
