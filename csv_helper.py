import csv
from Model import Pen, Pencil, Eraser, Scale, Sharpener

def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            prod_id = row[0]
            prod_name = row[1]
            prod_price = float(row[2])
            prod_stock = int(row[3])
            if product_instance := create_product_instance(
                    prod_id, prod_name, prod_price, prod_stock):
                data.append(product_instance)
    return data


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
