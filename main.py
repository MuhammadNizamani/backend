from typing import Optional
from fastapi import FastAPI, Response, status
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


# creating post request


@app.post("/posts")
def get_post(post: Post):  # we want payload has title and content
    # print(post.dict())  # this convert pydantic in python dictionary
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 2000000)
    my_posts.append(post_dict)

    # i am sending data back data is python dict
    return {"new_message": post_dict}

# note for path parameter if we use other routes like /posts/new it will reffencce to the
# /posts/{id}" rouate to we should always move path parameter function to the bottom

# follwing method is for getting one user only


@app.get("/posts/{id}")  # we are using path parameter
def get_post(id: int, response: Response):  # here path parameter will convert into int
    post = find_post(id)
    if not post:  # if post not found then we are going to give 404 status to the server
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"post with id {id} was not found"}
    return {"post_detail": post}
