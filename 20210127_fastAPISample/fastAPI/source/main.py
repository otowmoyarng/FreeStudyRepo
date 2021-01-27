from fastapi import FastAPI

app = FastAPI(
    title="FastAPIサンプル",
    description="FastAPIのサンプルです。",
    version="α1.0"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}