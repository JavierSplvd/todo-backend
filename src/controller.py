from fastapi import APIRouter
from entities.item import Item

items_router = APIRouter(prefix="/items", tags=["items"])

@items_router.get("/{id}")
async def getItem() -> Item:
    return {"message": "Hello World"}


@items_router.get("/")
async def getListItems() -> list[Item]:
    return {"message": "Hello World"}


@items_router.put("/")
async def updateItem():
    return {"message": "Hello World"}


@items_router.delete("/")
async def deleteItem():
    return {"message": "Hello World"}
