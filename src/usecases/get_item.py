from data.ItemRepository import ItemRepository
from entities.item import Item


def get_item(item_id: str) -> Item | None:
    query_result = ItemRepository().get_item(item_id=item_id)
    if query_result is None:
        return None
    return Item(**query_result)
