import os
from psycopg2 import connect

conn = connect(
    host=os.environ["DB_HOST"],
    database=os.environ["DB_DATABASE"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
)


class ItemRepository:
    def __init__(self):
        print("ItemRepository instanced.")

    def get_item(self, item_id: str):
        cursor = conn.cursor()

        query = "SELECT * FROM items WHERE id = %s;"
        cursor.execute(query, (item_id,))
        columns = [desc[0] for desc in cursor.description]
        item = dict(zip(columns, cursor.fetchone()))

        cursor.close()

        print(item)

        return item

    def get_all_items(self):
        cursor = conn.cursor()

        query = "SELECT * FROM items ORDER BY created_at;"
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        items = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()

        print(items)

        return items
