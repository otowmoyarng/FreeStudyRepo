from enum import Enum
from fastapi import FastAPI
from typing import Optional

class ModelName(str, Enum):
    """[summary]
    Args:
        str ([type]): [description]
        Enum ([type]): [description]
    """    
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
    return {
        "message" : "Hello World"
    }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q : Optional[str] = None):
    if q:
        return {
            "item_id": item_id,
            "q": q
        }
    return {
        "item_id" : item_id
    }

@app.get("/users/me")
async def read_user_me():
    return {
        "user_id": "the current user"
    }

@app.get("/users/{user_id}")
async def read_user(user_id : str):
    return {
        "user_id": user_id
    }

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {
        "file_path" : file_path
    }

@app.get("/items/")
async def read_time(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]