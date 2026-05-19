from db import conn, cursor

def add_item(name, price, category):
    query = """
    INSERT INTO menu(item_name, price, category)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, category, price))
    conn.commit()

def view_menu():
    cursor.execute("SELECT * FROM menu")
    return cursor.fetchall()

def delete_item(item_id):

    cursor.execute(
        "DELETE FROM menu WHERE item_id=%s",
        (item_id,)
    )

    conn.commit()