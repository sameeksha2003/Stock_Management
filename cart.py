import stock

cart = []


def list_products():
    print("Available products:")
    for product in stock.stock_warehouse:
        print(f"Product: {product.pname}, Price: {product.price}")


def purchase(item, quant):
    found = next(filter(lambda n: n.pname == item,
                 stock.stock_warehouse), None)

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
    stock.save()
