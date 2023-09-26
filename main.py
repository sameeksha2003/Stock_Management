import argparse
import cart
import stock

parser = argparse.ArgumentParser(description="Stock management")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--owner", action="store_true",
                   help="Load owner interface")
group.add_argument("--customer", action="store_true",
                   help="Load customer interface")

args = parser.parse_args()

stock.load()

if args.owner:
    while True:
        print("\nShopkeeper's Interface:")
        print("1. List Stock")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Save stock")
        print("5. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                stock.listStock()
            case "2":
                stock.add()
            case "3":
                item = input("Enter the product name: ")
                quant = int(input("Enter the quantity: "))
                stock.remove(item, quant)
            case "4":
                stock.save()
                print("Stock saved")
            case "5":
                break
            case _:
                print("Invalid choice")

elif args.customer:
    while True:
        print("\nCustomer's Interface:")
        print("1. List Stock")
        print("2. Purchase Stock")
        print("3. Show Cart")
        print("4. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                cart.list_products()
            case "2":
                item = input("Enter the product name: ")
                quant = int(input("Enter the quantity: "))
                cart.purchase(item, quant)
            case "3":
                cart.show_cart()
            case "4":
                break
            case  _:
                print("Invalid choice")
