from fastapi import APIRouter
from entities.item import Item
from usecases.get_item import get_item
from usecases.get_list_items import get_list_items
from usecases.update_item import update_item
from usecases.delete_item import delete_item
from usecases.create_item import create_item

items_router = APIRouter(prefix="/items", tags=["items"])


@items_router.get("/{item_id}")
async def get_item_route(item_id: str) -> Item | None:
    return get_item(item_id)


@items_router.get("/")
async def get_items_route() -> list[Item]:
    return get_list_items()


@items_router.put("/")
async def put_item_ruote(item: Item):
    return update_item(item.id, item.title)


@items_router.post("/")
async def post_item_ruote(item: Item):
    return create_item(item.title)


@items_router.delete("/{item_id}")
async def delete_item_route(item_id: str):
    return delete_item(item_id)
