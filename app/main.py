from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body  # bofy is used for reciveing data from frontend
from pydantic import BaseModel  # this libaray is for setting schema
# couse I can create random  ID couse I am not using DB right now
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import time
from . import model
from .database import engine, get_db

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


# here I have created post class which inherites basemodel which help me
#  to set schema for post request
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # here user did not provide published then it will be true
    # here i have created field which completly  optional


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='admin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful!")
        break
    except Exception as error:
        print("Database fail to connect")
        print("error is ", error)
        time.sleep(3)


my_posts = [{"title": "6 sahur", "content": "I am fasting in ramzan", "id": 1},
            {"title": "6 Iftari", "content": "I like Pakurha", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
# request come in get methnd and url "/"


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}

# here I am going to running samples


# creating post request


# chnaging defualt status to create status which 201
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):  # we want payload has title and content
    # print(post.dict())  # this convert pydantic in python dictionary
    cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s,%s) RETURNING * """,
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()  # any time we need to insert data we have to commit it.

    # i am sending data back data is python dict
    return {"new_message": new_post}

# note for path parameter if we use other routes like /posts/new it will reffencce to the
# /posts/{id}" rouate to we should always move path parameter function to the bottom

# follwing method is for getting one user only


@app.get("/posts/{id}")  # we are using path parameter
def get_post(id: int):  # here path parameter will convert into int
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()

    if not post:  # if post not found then we are going to give 404 status to the server
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id {id} was not found"}
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute(
        """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    # when you are deleting somthing you are not allow to pass some data in FastAPI
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    return {"status": "succes"}


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s , content = %s, 
    published = %s WHERE id =%s  RETURNING *""", (post.title, post.content, post.published, str(id),))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    return {"data": updated_post}
