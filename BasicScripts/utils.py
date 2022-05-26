from passlib.context import CryptContext

pwd_hash = CryptContext(deprecated='auto', schemes=['bcrypt'])


def hash_pssd(pwd: str):
    return pwd_hash.hash(pwd)


def verify_password(hashed: str, absolute: str):
    return pwd_hash.verify(hashed, absolute)


if __name__ == '__main__':
    a = '$2b$12$qW3lUxEosBQ4fxGdTRAjwO0HN2I6obKBo6wDTAEi/YshszoRAjncS'
    b = '$enter_password$'
    print(hash_pssd(b))
    print(verify_password(hash_pssd(b), b))
