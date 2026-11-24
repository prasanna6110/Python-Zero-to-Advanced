# Day 098 · Databases with sqlite3 — Joins, aggregates and Row objects
# Run: python example_2.py

import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
conn.executescript("""
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL);
INSERT INTO customers VALUES (1, 'Asha'), (2, 'Ravi');
INSERT INTO orders (customer_id, amount) VALUES (1, 500), (1, 1200), (2, 300);
""")
query = """
SELECT c.name, COUNT(o.id) AS n_orders, SUM(o.amount) AS total
FROM customers c JOIN orders o ON o.customer_id = c.id
GROUP BY c.id ORDER BY total DESC
"""
for row in conn.execute(query):
    print(f"{row['name']}: {row['n_orders']} orders, ₹{row['total']:.0f}")
conn.close()
