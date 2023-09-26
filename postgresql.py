import psycopg2
import csv

db_params = {
    'dbname': 'stock',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def initialize_database(db_params):
    try:
        conn = psycopg2.connect(**db_params)
        conn.autocommit=True
        cursor=conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS public.stock (
                ProductID TEXT PRIMARY KEY,
                ProductName TEXT,
                ProductPrice REAL,
                ProductStock INTEGER
            )
        ''')
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def insert_or_update(db_params, csv_file):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        with open(csv_file, 'r',encoding='UTF-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader) 
            for row in csv_reader:
                product_id, product_name, product_price, new_stock = row

                cursor.execute("SELECT * FROM stock WHERE ProductID=%s", (product_id,))
                existing_product = cursor.fetchone()

                if existing_product:
                    updated_stock = existing_product[3] + int(new_stock)
                    cursor.execute("UPDATE stock SET ProductStock=? WHERE ProductID=%s",(updated_stock, product_id))
                    conn.commit()
                else:
                    cursor.execute("INSERT INTO stock (ProductID, ProductName, ProductPrice, ProductStock) VALUES (%s, %s, %s, %s)",
                                   (product_id, product_name, product_price, int(new_stock)))

        conn.commit()
        print("Stock Updated from CSV")
    except FileNotFoundError:
        print("CSV file not found.")
    finally:
        conn.close()



def read_sql(db_params):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock")
    data = cursor.fetchall()
    conn.close()
    return data


def write_sql(db_params, data):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    try:
        for product in data:
            cursor.execute("""
                INSERT INTO stock (ProductID, ProductName, ProductPrice, ProductStock)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (ProductID) DO UPDATE
                SET ProductName=EXCLUDED.ProductName,
                    ProductPrice=EXCLUDED.ProductPrice,
                    ProductStock=EXCLUDED.ProductStock
            """, (product.pid, product.pname, product.price, product.stock))

        conn.commit()
        print("Data inserted or updated successfully.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()
