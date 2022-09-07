from fastapi import FastAPI
from app.api.rooters import programmers

app = FastAPI()

# @app.get("/")
# def index():
#     return {"message": "Hello world"}
app.include_router(
    programmers.rooter,
    prefix="/api/programmers",
    tags=["programmers"]
)
