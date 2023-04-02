
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db
# now on I am going to create functions for users table

router = APIRouter(prefix="/users",  # I am using /users everywhere so i make a prefix that handles that now i just need to write /
                   # this will create a group in api doc for post opretion
                   tags=["users"]
                   )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.userOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.userOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} do exist")
    return user
