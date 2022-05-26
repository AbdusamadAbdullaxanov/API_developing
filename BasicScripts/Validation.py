from pydantic import BaseModel, EmailStr, conint
from typing import Optional


class Posts(BaseModel):
    title: str
    content: str
    published: bool


class Votes(BaseModel):
    post_id: int
    like: conint(le=1)


class User_validation(BaseModel):
    mail: EmailStr
    password: str


class CreatePosts(Posts):
    pass


class UpdatePosts(Posts):
    pass


class SignUp(BaseModel):
    token: str


class TokenData(BaseModel):
    token: Optional[str] = None
