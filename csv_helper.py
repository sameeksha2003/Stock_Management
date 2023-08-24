import csv
from Model import Pen, Pencil, Eraser, Scale, Sharpener


def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == "pen":
                data.append(Pen(row[0], row[1], int(row[2]), int(row[3])))
            elif row[1] == "pencil":
                data.append(Pencil(row[0], row[1], int(row[2]), int(row[3])))
            elif row[1] == "eraser":
                data.append(Eraser(row[0], row[1], int(row[2]), int(row[3])))
            elif row[1] == "scale":
                data.append(Scale(row[0], row[1], int(row[2]), int(row[3])))
            elif row[1] == "sharpener":
                data.append(Sharpener(row[0], row[1],
                            float(row[2]), int(row[3])))
    return data


def write_csv(file_path, data, fieldnames):
    with open(file_path, 'w', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in data:
            writer.writerow({
                "ProductID": product.pid,
                "ProductName": product.pname,
                "ProductPrice": product.price,
                "ProductStock": product.stock
            })
