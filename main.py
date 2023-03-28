from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body  # bofy is used for reciveing data from frontend
from pydantic import BaseModel  # this libaray is for setting schema
app = FastAPI()


# here I have created post class which inherites basemodel which help me
#  to set schema for post request
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # here user did not provide published then it will be true
    # here i have created field which completly  optional
    rating: Optional[int] = None

# request come in get methnd and url "/"


@app.get("/")
async def root():
    return {"message": "trying to create FastAPI"}

# here I am going to running samples


@app.get("/data")
def get_data():
    return {"name": "Ishaque", "friendname": "Ahmed, Salman, Sarwan, Anshal"}

# creating post request


@app.post("/createpost")
def get_post(post: Post):  # we want payload has title and content
    print(post)  # new_post is a pydantic type it can be converted
    print(post.dict())  # this convert pydantic in python dictionary

    # i am sending data back data is python dict
    return {"new_message": post}
