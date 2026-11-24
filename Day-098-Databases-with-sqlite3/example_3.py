# Day 098 · Databases with sqlite3 — Transactions and SQL injection
# Run: python example_3.py

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE accounts (name TEXT PRIMARY KEY, balance INTEGER CHECK(balance >= 0))")
conn.executemany("INSERT INTO accounts VALUES (?, ?)", [("A", 100), ("B", 50)])
conn.commit()

def transfer(src, dst, amount):
    try:
        with conn:                                   # atomic transaction
            conn.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, dst))
            conn.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, src))
        print(f"transferred {amount}")
    except sqlite3.IntegrityError:
        print(f"transfer of {amount} failed -> rolled back")

transfer("A", "B", 30)
transfer("A", "B", 500)
print(conn.execute("SELECT * FROM accounts").fetchall())

evil = "x' OR '1'='1"
unsafe = f"SELECT * FROM accounts WHERE name = '{evil}'"
print("UNSAFE query returns:", conn.execute(unsafe).fetchall())
print("SAFE query returns  :", conn.execute("SELECT * FROM accounts WHERE name = ?", (evil,)).fetchall())
