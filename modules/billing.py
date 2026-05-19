from db import conn, cursor

def create_order(customer, table_no,
                 total, gst, final_amount):

    query = """
    INSERT INTO orders(
        customer_name,
        table_no,
        total_amount,
        gst,
        final_amount
    )
    VALUES(%s,%s,%s,%s,%s)
    RETURNING order_id
    """

    cursor.execute(
        query,
        (
            customer,
            table_no,
            total,
            gst,
            final_amount
        )
    )

    order_id = cursor.fetchone()[0]

    conn.commit()

    return order_id