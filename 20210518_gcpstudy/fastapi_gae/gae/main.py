from fastapi import FastAPI

app = FastAPI(
    title="FastAPISample",
    description="GoogleAppEngineで起動するFastAPIのサンプルです。",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"hello": "world"}
