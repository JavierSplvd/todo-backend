import os
from psycopg2 import connect
from uuid import uuid4

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

    def create_item(self, title: str, done: str):
        cursor = conn.cursor()

        query = "INSERT INTO items (id, title, done) VALUES (%s, %s, %s);"
        cursor.execute(
            query,
            (str(uuid4()), title, done),
        )
        conn.commit()

        cursor.close()

        return

    def update_item(self, item_id: str, new_title: str, new_done_status: bool):
        cursor = conn.cursor()

        query = "UPDATE items SET title = %s, done = %s WHERE id = %s;"
        cursor.execute(query, (new_title, new_done_status, item_id))
        conn.commit()

        cursor.close()

        return

    def get_all_items(self, title: str | None):
        cursor = conn.cursor()

        if title is None:
            query = "SELECT * FROM items ORDER BY created_at;"
            cursor.execute(query)
        else:
            query = "SELECT * FROM items WHERE title ILIKE %s ORDER BY created_at;"
            cursor.execute(query, ("%" + title + "%",))
        columns = [desc[0] for desc in cursor.description]
        items = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()

        print(items)

        return items
