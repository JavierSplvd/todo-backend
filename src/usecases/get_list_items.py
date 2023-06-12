from data.ItemRepository import ItemRepository
from entities.item import Item


def get_list_items(title: str | None) -> list[Item]:
    return ItemRepository().get_all_items(title)
