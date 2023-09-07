from Model import Pen, Pencil, Eraser, Scale, Sharpener
from csv_helper import read_csv, write_csv
import datetime

def log(func):
    def wrapper(*args, **kwargs):
        timestamp=datetime.datetime.now()
        function_name=func.__name__
        log_file=f'{timestamp}-{function_name}called\n'

        with open('log.txt','a',encoding='UTF-8') as file:
            file.write(log_file)

        return func(*args, **kwargs)
    return wrapper


stock_warehouse = []

@log
def load(filename):
    stock_data = read_csv(filename)
    for product in stock_data:
        prod_id = product.pid
        prod_name = product.pname
        prod_price = float(product.price)
        prod_stock = int(product.stock)

        if product_instance := create_product_instance(
                prod_id, prod_name, prod_price, prod_stock):

            stock_warehouse.append(product_instance)

@log
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
        

@log
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

@log
def remove(product_id, quant):
    found = next(filter(lambda product: product.pname.lower() == product_id.lower(), stock_warehouse), None)
    
    if found:
        if found.stock >= quant:
            choice = input("Enter your choice (reduce/remove): ").lower()
            if choice == 'reduce':
                found.stock -= quant
                print("Reduced")
            elif choice == 'remove':
                stock_warehouse.remove(found)
                print("Removed")
            else:
                print("Invalid choice")
        else:
            print("Not enough stock")
    else:
        print("Product not found")



@log
def save():
    fieldnames = ["ProductID", "ProductName", "ProductPrice", "ProductStock"]
    stock_data = stock_warehouse
    write_csv('stock.csv',
              stock_data, fieldnames)
