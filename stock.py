from Model import Pen, Pencil, Eraser, Scale, Sharpener
from sql_helper import read_sql, write_sql, insert_or_update,initialize_database
from logger import log

stock_warehouse = []


def load(db_file):

    initialize_database(db_file)
    
    stock_data = read_sql(db_file)
    for product in stock_data:
        prod_id, prod_name, prod_price, prod_stock = product
        if product_instance := create_product_instance(
            prod_id, prod_name, prod_price, prod_stock
        ):
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


@log
def listStock():
    print("The available products in stock:")
    stock_data = read_sql('stock.db')
    for product in stock_data:
        print(f"Product: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}")

@log
def add():
    print("Choose the file from which you want to insert or update stock:")
    print("1. stock.csv")
    print("2. Another CSV file")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        csv_file = 'stock.csv'
        print("Stock Added")
    elif choice == '2':
        csv_file = input("Enter the path to the CSV file: ")
        print("Stock Added")
    else:
        print("Invalid choice")
        return

    insert_or_update('stock.db', csv_file)

@log
def remove(product_id, quant):
    found = next(filter(lambda product: product.pname.lower()
                 == product_id.lower(), stock_warehouse), None)

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
    stock_data = stock_warehouse

    write_sql('stock.db',
              stock_data)

