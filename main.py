from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()
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
def get_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "post is created successfully"}
