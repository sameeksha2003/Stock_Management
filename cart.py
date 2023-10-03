import stock
from logger import log

cart = []


@log
def list_products()->None:
    print("Available products:")
    for product in stock.stock_warehouse:
        print(f"Product: {product.pname} at Price: {product.price}")


@log
def purchase(item: str, quant: int)->None:
    found = next(filter(lambda n: n.pname == item, stock.stock_warehouse), None)
    if found:
        if found.stock >= quant:
            cart.append({"item": found, "Quantity": quant})
            found.stock -= quant
            print(f"Added {quant} {item} to cart.")
        else:
            print("Not enough stock for", item)
    else:
        print("Product not found")

@log
def show_cart()->None:
    total=0.0
    for item in cart:
        product = item["item"]
        price = product.price
        quant = item["Quantity"]
        prod_tot = price*quant
        print(f"{product.pname} {price:.1f} x {quant} = {prod_tot:.1f}")
        total += prod_tot
    print(f"Total:{total:.1f}")
