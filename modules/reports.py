from db import cursor

def sales_report():

    cursor.execute(
        "SELECT * FROM orders"
    )

    return cursor.fetchall()