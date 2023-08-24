import stock
import argparse

parser = argparse.ArgumentParser(description="Stock management")
parser.add_argument("--stock", nargs="+",
                    help="CSV files",required=True)

args = parser.parse_args()

if args.stock:
    for stock_file in args.stock:
        stock.load(stock_file)
else:
    parser.print_help()

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
