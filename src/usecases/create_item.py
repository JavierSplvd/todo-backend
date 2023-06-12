from data.ItemRepository import ItemRepository


def create_item(title: str, done: str):
    repo = ItemRepository()
    return repo.create_item(title, done)
