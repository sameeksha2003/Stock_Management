from Model import Pen, Pencil, Eraser, Scale, Sharpener
from csv_helper import read_csv, write_csv

stock_warehouse = []


def load(filename):
    stock_data = read_csv(filename)
    for product in stock_data:
        prod_id = product.pid
        prod_name = product.pname
        prod_price = float(product.price)
        prod_stock = int(product.stock)

        product_instance = create_product_instance(
            prod_id, prod_name, prod_price, prod_stock)

        if product_instance:
            stock_warehouse.append(product_instance)


def create_product_instance(prod_id, prod_name, prod_price, prod_stock):
    match prod_id:
        case "P1":
            return Pen(prod_id, prod_name, prod_price, prod_stock)
        case "P2":
            return Pencil(prod_id, prod_name, prod_price, prod_stock)
        case "P3":
            return Eraser(prod_id, prod_name, prod_price, prod_stock)
        case "P4":
            return Scale(prod_id, prod_name, prod_price, prod_stock)
        case "P5":
            return Sharpener(prod_id, prod_name, prod_price, prod_stock)
        case _:
            return None


def listStock():
    print("The available products in stock:")
    for prods in stock_warehouse:
        print(
            f"Product: {prods.pid}, Name: {prods.pname}, Price: {prods.price}, Stock: {prods.stock}")


def add(file):
    new_stock = read_csv(file)
    for product in new_stock:
        product_id = product.pid
        stock = int(product.stock)
        print("Adding stock for Product ID:", product_id, "Stock:", stock)
        stock_pid = list(
            filter(lambda n: n.pid == product_id, stock_warehouse))
        if stock_pid:
            stock_pid[0].stock += stock
            print("Stock added for:",
                  stock_pid[0].pid, "New stock:", stock_pid[0].stock)


def save():
    fieldnames = ["ProductID", "ProductName", "ProductPrice", "ProductStock"]
    stock_data = stock_warehouse
    write_csv('stock.csv', stock_data, fieldnames)
