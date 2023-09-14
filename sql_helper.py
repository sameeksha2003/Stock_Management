import sqlite3
import csv


def initialize_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS stock (
        ProductID TEXT PRIMARY KEY,
        ProductName TEXT,
        ProductPrice REAL,
        ProductStock INTEGER
    )''')
    
    conn.commit()
    conn.close()


def insert_or_update(db_file, csv_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  
            for row in csv_reader:
                product_id, product_name, product_price, new_stock = row
                cursor.execute("SELECT * FROM stock WHERE ProductID=?", (product_id,))
                existing_product = cursor.fetchone()

                if existing_product:
                    updated_stock = existing_product[3] + int(new_stock)
                    cursor.execute(
                        "UPDATE stock SET ProductStock=? WHERE ProductID=?", (updated_stock, product_id))
                else:
                    cursor.execute("INSERT INTO stock (ProductID, ProductName, ProductPrice, ProductStock) VALUES (?, ?, ?, ?)",
                                   (product_id, product_name, product_price, int(new_stock)))

        conn.commit()
        print("Stock Updated from CSV")
    except FileNotFoundError:
        print("CSV file not found.")
    finally:
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
