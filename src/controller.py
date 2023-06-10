from fastapi import APIRouter
from entities.item import Item
from usecases.get_item import get_item
from usecases.get_list_items import get_list_items

items_router = APIRouter(prefix="/items", tags=["items"])


@items_router.get("/{item_id}")
async def getItem(item_id: str) -> Item | None:
    return get_item(item_id)


@items_router.get("/")
async def getListItems() -> list[Item]:
    return get_list_items()


@items_router.put("/")
async def updateItem():
    return {"message": "Hello World"}


@items_router.delete("/")
async def deleteItem():
    return {"message": "Hello World"}
