from data.ItemRepository import ItemRepository


def create_item(title: str):
    repo = ItemRepository()
    return repo.create_item(title)
