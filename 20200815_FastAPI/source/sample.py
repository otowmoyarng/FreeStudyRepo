from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

@app.get("/")
async def root():
    return {'message' : "Hello World"}

@app.get("/{id}")
async def getId(id : int):
    return {'id' : id}

@app.get("/items/")
async def read_items(q : List[str] = Query(None)):
    query_items = {'q' : q}
    return query_items

@app.post("/query")
async def query(
    name : str,
    age : int):
    return {'name' : name, 'age' : age}