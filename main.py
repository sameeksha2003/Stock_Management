import argparse
import cart
import stock
parser = argparse.ArgumentParser(description="Stock management")
parser.add_argument("--owner", action="store_true",
                    help="Load owner interface")
parser.add_argument("--customer", action="store_true",
                    help="Load customer interface")

args = parser.parse_args()

if args.owner:
    stock.load('stock.csv')
    while True:
        print("\nShopkeeper's Interface:")
        print("1. List Stock")
        print("2. Add Stock")
        print("3. Save Stock")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock.listStock()
        elif choice == "2":
            file_choice = input(
                "Enter the file from where you want to add stocks: ")
            stock.add(file_choice)
            print("Stock added")
        elif choice == "3":
            stock.save()
            print("Stock saved")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

elif args.customer:
    cart.load('stock.csv')
    while True:
        print("\nCustomer's Interface:")
        print("1. List Stock")
        print("2. Purchase Stock")
        print("3. Save Cart")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            cart.list_products()
        elif choice == "2":
            item = input("Enter the product name: ")
            quant = int(input("Enter the quantity: "))
            cart.purchase(item, quant)
        elif choice == "3":
            cart.save_cart()
            print("Cart saved")
        elif choice == "4":
            break
        else:
            print("Invalid choice")
