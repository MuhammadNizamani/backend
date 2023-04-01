from pydantic import BaseModel  # this libaray is for setting schema
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


class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime

    class Config:
        orm_mode = True
