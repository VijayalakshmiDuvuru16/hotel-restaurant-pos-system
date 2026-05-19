import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="hotel_pos",
    user="postgres",
    password="Vijaya16",
    port="5432"
)

cursor = conn.cursor()