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
        result = cursor.fetchone()
        if result is None:
            return
        item = dict(zip(columns, result))

        cursor.close()

        print(item)

        return item

    def delete_item(self, item_id: str):
        cursor = conn.cursor()

        query = "DELETE FROM items WHERE id = %s;"
        cursor.execute(query, (item_id,))
        conn.commit()

        cursor.close()

        return

    def update_item(self, item_id: str, new_title: str):
        cursor = conn.cursor()

        query = "UPDATE items SET title = %s WHERE id = %s;"
        cursor.execute(query, (new_title, item_id))
        conn.commit()

        cursor.close()

        return

    def get_all_items(self):
        cursor = conn.cursor()

        query = "SELECT * FROM items ORDER BY created_at;"
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        items = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()

        print(items)

        return items
