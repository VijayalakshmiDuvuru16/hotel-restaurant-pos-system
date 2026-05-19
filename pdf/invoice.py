from reportlab.pdfgen import canvas

def generate_invoice(order_id, customer, amount):

    file_name = f"invoice_{order_id}.pdf"

    c = canvas.Canvas(file_name)

    c.drawString(100, 800, "HOTEL POS SYSTEM")
    c.drawString(100, 770, f"Order ID: {order_id}")
    c.drawString(100, 740, f"Customer: {customer}")
    c.drawString(100, 710, f"Total Amount: Rs.{amount}")

    c.save()

    return file_name