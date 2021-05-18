from fastapi import FastAPI
import os


apiVersion = os.getenv("API_VERSION", "1.0.0")

app = FastAPI(
    title="FastAPISample",
    description="GoogleAppEngineで起動するFastAPIのサンプルです。",
    version=apiVersion
)


@app.get("/")
async def root():
    return {
        "hello": "world"
    }


@app.get("/test")
async def test(param: str = "NoParam"):
    return {
        "code": "200",
        "param": param,
        "version": apiVersion
    }
