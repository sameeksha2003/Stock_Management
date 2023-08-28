import argparse
import cart
import stock
parser = argparse.ArgumentParser(description="Stock management")
group=parser.add_mutually_exclusive_group(required=True)
group.add_argument("--owner", action="store_true",
                    help="Load owner interface")
group.add_argument("--customer", action="store_true",
                    help="Load customer interface")

args = parser.parse_args()
stock.load('stock.csv')

if args.owner:
    while True:
        print("\nShopkeeper's Interface:")
        print("1. List Stock")
        print("2. Add Stock")
        print("3. Save Stock")
        print("4. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                stock.listStock()
            case "2":
                file_choice = input(
                    "Enter the file from where you want to add stocks: ")
                stock.add(file_choice)
                print("Stock added")
            case "3":
                stock.save()
                print("Stock saved")
            case "4":
                break
            case _:
                print("Invalid choice")

elif args.customer:
    while True:
        print("\nCustomer's Interface:")
        print("1. List Stock")
        print("2. Purchase Stock")
        print("3. Save Cart")
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
                cart.save_cart()
                print("Cart saved")
            case "4":
                break
            case  _:
                print("Invalid choice")

else:
    parser.print_help()
