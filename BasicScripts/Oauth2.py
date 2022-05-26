from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from config import settings

scheme = OAuth2PasswordBearer(tokenUrl='users')
SECRET_KEY = settings.access_key
ALGORITHM = settings.algorithm
EXPIRETIMES = settings.expire_time
COPY = ""


def encoder(item: dict):
    return jsonable_encoder(item)


def access_token(dictdata: dict):
    expire = datetime.now() + timedelta(seconds=EXPIRETIMES)
    dictdata.update({"email": dictdata.get('email'), "password": dictdata.get("password"), "exp": expire})
    return jwt.encode(dictdata, SECRET_KEY, algorithm=ALGORITHM)


def verify(token: str, credential_error):
    try:
        global COPY
        COPY += str(token)
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_num = decoded.get("email")
        if id_num is None:
            raise credential_error
    except JWTError as error:
        credential_error.detail = str(error)
        raise credential_error

    print("value decoded " + str(decoded))
    print("type of decoded " + str(type(decoded)))
    return decoded


def get_current_user(recieve: str = Depends(scheme)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized account')
    print("recieve --> " + str(recieve))
    return verify(recieve, exception)


if __name__ == '__main__':
    code = {"email": "pythondeveloper441@gmail.com", "password": "$enter_password$"}
    # print(code)
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InB5dGhvbmRldmVsb3BlcjQ0MUBnbWFpbC5jb20iLCJwYXNzd29yZCI6IiRlbnRlcl9wYXNzd29yZCQiLCJleHAiOjE2NTMxNTAwMzR9.s6steOf_j7H81UA2lmdCv8OfZMua7BJDLLwKUtNvInY
    # print(access_token(code)
    get_current_user()
