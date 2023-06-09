# from fastapi.params import Body  # bofy is used for reciveing data from frontend
# couse I can create random  ID couse I am not using DB right now
from fastapi import FastAPI
from . import models
# from .database import engine
from .routers import user, post, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def default_message():
    return {"message": "welcome world"}
