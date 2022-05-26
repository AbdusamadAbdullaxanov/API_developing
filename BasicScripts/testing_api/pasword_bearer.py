from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = 'Private key'

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='random')


@app.get("/random")
def r():
    return {"sa": "dasdasd"}


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {'token': token}
