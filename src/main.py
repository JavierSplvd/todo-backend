from fastapi import FastAPI
from controller import items_router

app = FastAPI()

app.include_router(items_router)

@app.get("/health")
async def root():
    return {"message": "OK"}