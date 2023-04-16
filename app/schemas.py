from pydantic import BaseModel, EmailStr  # this libaray is for setting schema
from datetime import datetime
from typing import Optional
from pydantic.types import conint


# here I have created post class which inherites basemodel which help me
#  to set schema for post request
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # here user did not provide published then it will be true
    # here i have created field which completly  optional


class CreatePost(PostBase):
    pass


class userOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):  # here i am going to extend PostBase class so I don't have to repeat some code
    id: int
    created_at: datetime
    owner_id: int
    owner: userOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    Votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
