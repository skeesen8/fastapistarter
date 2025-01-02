from fastapi import FastAPI, Query

from pydantic import BaseModel

from typing import Annotated

from enum import Enum



app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


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

test add 

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item