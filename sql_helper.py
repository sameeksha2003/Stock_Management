import csv
import sqlite3


conn = sqlite3.connect('stock.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS stock (
                ProductID TEXT PRIMARY KEY,
                ProductName TEXT,
                ProductPrice REAL,
                ProductStock INTEGER
                )''')

conn.commit()
conn.close()


def import_csv_to_sqlite(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            cursor.execute("INSERT INTO stock VALUES (?, ?, ?, ?)", row)

    conn.commit()
    conn.close()


def read_sql(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock")
    data = cursor.fetchall()
    conn.close()
    return data


def write_sql(db_file, data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    data_ele = [(product.pid, product.pname, product.price,
                    product.stock) for product in data]
    cursor.executemany(
        "INSERT OR REPLACE INTO stock (ProductID, ProductName, ProductPrice, ProductStock) VALUES (?, ?, ?, ?)",
        data_ele
    )

    conn.commit()
    conn.close()


def insert_or_update(product_id, new_stock):
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stock WHERE ProductID=?", (product_id,))
    existing_product = cursor.fetchone()

    if existing_product:
        updated_stock = existing_product[3] + new_stock
        cursor.execute(
            "UPDATE stock SET ProductStock=? WHERE ProductID=?", (updated_stock, product_id))
    else:
        cursor.execute("INSERT INTO stock (ProductID, ProductName, ProductPrice, ProductStock) VALUES (?, ?, ?, ?)",
                       (product_id, "", 0.0, new_stock))

    conn.commit()
    conn.close()
