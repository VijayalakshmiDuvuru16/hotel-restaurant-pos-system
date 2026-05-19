import streamlit as st
import psycopg2

from modules.menu import *
from modules.billing import *


# DATABASE CONNECTION
conn = psycopg2.connect(
    host="localhost",
    database="hotel_pos",
    user="postgres",
    password="your_password"
)

cursor = conn.cursor()


# CREATE ORDER FUNCTION
def create_order(customer, table_no, total, gst, final_amount):

    query = """
    INSERT INTO orders
    (customer_name, table_no, total_amount, gst, final_amount)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING order_id
    """

    cursor.execute(
        query,
        (customer, table_no, total, gst, final_amount)
    )

    order_id = cursor.fetchone()[0]

    conn.commit()

    return order_id

st.title("Hotel & Restaurant POS")

menu_option = st.sidebar.selectbox(
    "Menu",
    [
        "Add Item",
        "View Menu",
        "Delete Item",
        "Create Bill"
    ]
)

# ADD ITEM
if menu_option == "Add Item":

    st.header("Add Food Item")

    name = st.text_input("Item Name")
    category = st.text_input("Category")
    price = st.number_input("Price")

    if st.button("Add"):

        add_item(name, category, price)

        st.success("Item Added Successfully")

# VIEW MENU
elif menu_option == "View Menu":

    st.header("Menu List")

    data = view_menu()

    st.table(data)

# DELETE ITEM
elif menu_option == "Delete Item":

    st.header("Delete Item")

    item_id = st.number_input("Item ID")

    if st.button("Delete"):

        delete_item(item_id)

        st.success("Deleted Successfully")

# BILLING
elif menu_option == "Create Bill":

    st.header("Billing")

    customer = st.text_input("Customer Name")

    table_no = st.number_input("Table Number")

    total = st.number_input("Total Amount")

    gst = total * 0.18

    final_amount = total + gst

    st.write("GST:", gst)

    st.write("Final Amount:", final_amount)

    if st.button("Generate Bill"):

        order_id = create_order(
            customer,
            table_no,
            total,
            gst,
            final_amount
        )

        st.success(f"Bill Generated. Order ID: {order_id}")