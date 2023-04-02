from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body  # bofy is used for reciveing data from frontend
# couse I can create random  ID couse I am not using DB right now
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import time
from . import models
from .database import engine
from .routers import user, post, auth


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


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


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
