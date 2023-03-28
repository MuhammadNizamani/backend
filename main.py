from fastapi import FastAPI
from fastapi.params import Body  # bofy is used for reciveing data from frontend
from pydantic import BaseModel  # this libaray is for setting schema
app = FastAPI()


# here I have created post class which inherites basemodel which help me
#  to set schema for post request
class Post(BaseModel):
    title: str
    content: str

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
def get_post(new_post: Post):  # we want payload has title and content
    print(new_post.title)
    return {"new_message": "new post"}
