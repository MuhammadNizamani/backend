from .. import models, schemas
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
# request come in get methnd and url "/"
from typing import List


router = APIRouter(prefix="/posts",  # I am using /posts everywhere so i make a prefix that handles that now i just need to write /
                   # this will create a group in api doc for post opretion
                   tags=["posts"]
                   )


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts

# here I am going to running samples


# creating post request


# chnaging defualt status to create status which 201
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# we want payload has title and content
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    # # print(post.dict())  # this convert pydantic in python dictionary
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s,%s) RETURNING * """,
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()  # any time we need to insert data we have to commit it.

    # # i am sending data back data is python dict
    # we will use pydicnt to create post request
    # print(**post.dict())  # we are going to use dictiony unpaking here
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

# note for path parameter if we use other routes like /posts/new it will reffencce to the
# /posts/{id}" rouate to we should always move path parameter function to the bottom

# follwing method is for getting one user only


# we are using path parameter
@router.get("/{id}", response_model=schemas.Post)
# here path parameter will convert into int
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:  # if post not found then we are going to give 404 status to the server
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id {id} was not found"}
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    # cursor.execute(
    #     """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit

    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    # when you are deleting somthing you are not allow to pass some data in FastAPI
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.CreatePost, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s , content = %s,
    # published = %s WHERE id =%s  RETURNING *""", (post.title, post.content, post.published, str(id),))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
