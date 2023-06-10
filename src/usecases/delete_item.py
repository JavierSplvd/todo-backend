from data.ItemRepository import ItemRepository


def delete_item(item_id: str):
    return ItemRepository().delete_item(item_id)
