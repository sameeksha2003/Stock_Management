from csv_helper import write_csv
import stock

cart = []


def list_products():
    print("Available products:")
    for product in stock.stock_warehouse:
        print(f"Product: {product.pname}, Price: {product.price}")


def purchase(item, quant):
    found = None
    for product in stock.stock_warehouse:
        if product.pname == item:
            found = product
            break

    if found:
        if found.stock >= quant:
            cart.append({"item": found, "Quantity": quant})
            found.stock -= quant
            print(f"Added {quant} {item} to cart.")
        else:
            print("Not enough stock for", item)
    else:
        print("Product not found:", item)


def save_cart():
    fieldnames = ["ProductID", "ProductName", "ProductPrice", "ProductStock"]
    cart_data = []
    cart_data = stock.stock_warehouse
    write_csv('stock.csv',
              cart_data, fieldnames)
