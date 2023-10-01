import sqlite3 as sql

with sql.connect('product_db.db') as conn:
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pname TEXT NOT NULL,
        price INTEGER DEFAULT 0,
        type TEXT NOT NULL);
    """)

    cur.execute("""
    INSERT INTO products (pname, price, type)
    """)
