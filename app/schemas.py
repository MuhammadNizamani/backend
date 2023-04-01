from pydantic import BaseModel, EmailStr  # this libaray is for setting schema
from datetime import datetime


# here I have created post class which inherites basemodel which help me
#  to set schema for post request
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # here user did not provide published then it will be true
    # here i have created field which completly  optional


class CreatePost(PostBase):
    pass


class Post(PostBase):  # here i am going to extend PostBase class so I don't have to repeat some code
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class userOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
