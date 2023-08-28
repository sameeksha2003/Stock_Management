from csv_helper import read_csv, write_csv
from Model import Pen, Pencil, Eraser, Scale, Sharpener

stock_warehouse = []
cart = []


def load(filename):
    cart_data = read_csv(filename)
    for item in cart_data:
        prod_id = item.pid
        prod_name = item.pname
        prod_price = float(item.price)
        prod_stock = int(item.stock)

        product_instance = create_product_instance(
            prod_id, prod_name, prod_price, prod_stock)

        if product_instance:
            stock_warehouse.append(product_instance)


def create_product_instance(prod_id, prod_name, prod_price, prod_stock):
    if prod_id == "P1":
        return Pen(prod_id, prod_name, prod_price, prod_stock)
    elif prod_id == "P2":
        return Pencil(prod_id, prod_name, prod_price, prod_stock)
    elif prod_id == "P3":
        return Eraser(prod_id, prod_name, prod_price, prod_stock)
    elif prod_id == "P4":
        return Scale(prod_id, prod_name, prod_price, prod_stock)
    elif prod_id == "P5":
        return Sharpener(prod_id, prod_name, prod_price, prod_stock)
    else:
        return None


def list_products():
    print("Available products:")
    for product in stock_warehouse:
        print(f"{product.pname}: Rs.{product.price:.2f}")


def purchase(item, quant):
    found = None
    for product in stock_warehouse:
        if product.pname == item:
            found = product
            break

    if found:
        if found.stock >= quant:
            cart.append({"item": found, "Quantity": quant})
            found.stock -= quant
            print("Item is added to cart")
        else:
            print("Not enough stock")
    else:
        print("Product not found")


def save_cart():
    fieldnames = ["Item", "Quantity"]
    stock_data = [
        {
            "Item": product["item"].pname,
            "Quantity": product["Quantity"]
        }
        for product in cart
    ]
    write_csv('stock.csv', stock_data, fieldnames)
