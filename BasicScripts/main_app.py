from fastapi import FastAPI, Depends
from Database import Function
from Oauth2 import access_token
from fastapi.security import OAuth2PasswordRequestForm
from posts import router
from votes import router as route
from fastapi.middleware.cors import CORSMiddleware
origins = ["https://www.google.com"]
application = FastAPI()
application.include_router(router)
application.include_router(route)
application.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)


@application.post("/users/signup")
def addin(user: OAuth2PasswordRequestForm = Depends()):
    new_user = Function()
    return {"access_token": new_user.signup(user.username, user.password)}


@application.post('/users')
def log_in(user: OAuth2PasswordRequestForm = Depends()):
    hardcode = {"username": user.username, "password": user.password}
    check = access_token(hardcode)
    users = Function()
    return users.verify_acount(str(check))
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaWNlIiwicGFzc3dvcmQiOiJmYWtlaGFzaGVkc2VjcmV0MiIsImV4cCI6MTY1Mjc4NzgxOH0.3RUuSTOn2qyuK0ChZlDlCHkGT_oyKXJwPwez4_sAoYo"
