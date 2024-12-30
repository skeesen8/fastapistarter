from fastapi import FastAPI

from enum import Enum



app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/")
async def root():
    return {"message": "this finally works"}


# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return{"model_name":model_name,"message":"Deep Learngin FTW!"}
    if model_name.value == "lenet":
        return {"model_name":model_name, "message": "LeCNN all the Images"}
    return{"model_name":model_name,"message":"Have SOme ReSiduALS"}

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item