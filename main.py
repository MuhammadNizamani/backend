from fastapi import FastAPI

app = FastAPI()
# request come in get methnd and url "/"


@app.get("/")
async def root():
    return {"message": "trying to create FastAPI"}

# here I am going to running sample get data function


@app.get("/data")
def get_data():
    return {"name": "Ishaque", "friendname": "Ahmed, Salman, Sarwan, Anshal"}


@app.post("/createpost")
def get_post():
    return {"message": "post is created successfully"}
