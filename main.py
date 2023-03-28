from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body  # bofy is used for reciveing data from frontend
from pydantic import BaseModel  # this libaray is for setting schema
# couse I can create random  ID couse I am not using DB right now
from random import randrange
app = FastAPI()


# here I have created post class which inherites basemodel which help me
#  to set schema for post request
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # here user did not provide published then it will be true
    # here i have created field which completly  optional
    rating: Optional[int] = None


my_posts = [{"title": "6 sahur", "content": "I am fasting in ramzan", "id": 1},
            {"title": "6 Iftari", "content": "I like Pakurha", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

# request come in get methnd and url "/"


@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# here I am going to running samples

# follwing method is for getting one user only


@app.get("/posts/{id}")  # we are using path parameter
def get_post(id):
    # should convert id into int becaue path parameter give us id in string
    post = find_post(int(id))
    return {"post_detail": post}


# creating post request


@app.post("/posts")
def get_post(post: Post):  # we want payload has title and content
    # print(post.dict())  # this convert pydantic in python dictionary
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 2000000)
    my_posts.append(post_dict)

    # i am sending data back data is python dict
    return {"new_message": post_dict}
