from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import items_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(items_router)


@app.get("/health")
async def root():
    return {"message": "OK"}
