import sqlite3 as sql
import os
from product import Product

print(os.getcwd())

products_list = [('стул', 1000, 'мебель для зала'), ('стол', 2500, 'мебель для зала'),
                 ('диван', 20000, 'мебель для зала')]

def add_product(prodduct):
    insert = f"""INSERT INTO products (pname, price, type) VALUES (
    '{prodduct.name}', '{prodduct.price}', '{prodduct.types}')"""
    return insert


with sql.connect('product_db.db') as conn:
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pname TEXT NOT NULL,
        price INTEGER DEFAULT 0,
        type TEXT NOT NULL);
    """)
    # - - - - - - - - - - Интерфейс по добавлению товара - - - - - - - - - - - - - #

    # for prodduct in products_list:
    #     prodduct = Product(prodduct[0], prodduct[1], prodduct[2])
    #     cur.execute(add_product(prodduct))

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    result = cur.execute("SELECT * FROM products")
    print(result.fetchall())
