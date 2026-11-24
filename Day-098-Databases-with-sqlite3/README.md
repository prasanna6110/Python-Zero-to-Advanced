# Day 098 · Databases with sqlite3

_Advanced_

## SQLite
A full SQL database stored in **one file**, built into Python. It's great for apps, prototypes and learning SQL.

```python
import sqlite3
conn = sqlite3.connect("app.db")     # or ":memory:"
cur = conn.cursor()
cur.execute("CREATE TABLE ...")
conn.commit()
conn.close()
```
## Essentials
- **Always use parameters**: `cur.execute("... WHERE id = ?", (uid,))`. This prevents **SQL injection**.
- `executemany()` inserts many rows at once.
- `fetchone()`, `fetchall()` and `fetchmany(n)` read results.
- `conn.row_factory = sqlite3.Row` lets you access columns by name.
- `with conn:` is a transaction: it commits on success and **rolls back** on error.
- For bigger apps, look at **SQLAlchemy** (an ORM) and **PostgreSQL**.

## Examples

### Example 1: CRUD operations  ([`example_1.py`](example_1.py))

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, branch TEXT, cgpa REAL)")
cur.executemany("INSERT INTO students (name, branch, cgpa) VALUES (?, ?, ?)",
                [("Asha", "EE", 9.1), ("Ravi", "CS", 8.4), ("Meera", "EE", 8.9)])
conn.commit()
cur.execute("UPDATE students SET cgpa = ? WHERE name = ?", (9.0, "Ravi"))
cur.execute("DELETE FROM students WHERE name = ?", ("Meera",))
for row in cur.execute("SELECT * FROM students ORDER BY cgpa DESC"):
    print(row)
conn.close()
```

### Example 2: Joins, aggregates and Row objects  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Transactions and SQL injection  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Build a library management system with `books` and `members` tables.
2. Write a function that exports any table to CSV.
3. Add an index and compare query speed on 100k rows.

---

[⬅ Day 097](../Day-097-Serialization-pickle-shelve-and-struct/README.md) · [🏠 Home](../README.md) · [Day 099 ➡](../Day-099-Networking-Sockets-HTTP-and-urllib/README.md)
