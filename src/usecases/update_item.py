from data.ItemRepository import ItemRepository


def update_item(item_id: str, new_title: str):
    repo = ItemRepository()
    if repo.get_item(item_id) is None:
        return
    return repo.update_item(item_id, new_title)
