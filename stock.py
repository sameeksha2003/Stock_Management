from Model import Pen, Pencil, Eraser, Scale, Sharpener
from sql_helper import read_sql, write_sql,insert_or_update
from logger import log
from csv_helper import read_csv

stock_warehouse = []


def load(filename):
    stock_data = read_sql(filename)
    for product in stock_data:
        prod_id = product[0]  
        prod_name = product[1]  
        prod_price = float(product[2])  
        prod_stock = int(product[3])  

        if product_instance := create_product_instance(
                prod_id, prod_name, prod_price, prod_stock):

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
    for prods in stock_warehouse:
        print(
            f"Product: {prods.pid}, Name: {prods.pname}, Price: {prods.price}, Stock: {prods.stock}")


@log
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
            insert_or_update(product_id, stock_pid[0].stock)
        else:
            print("Product not found")


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
