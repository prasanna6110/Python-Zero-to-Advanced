# Day 151 · Project: Inventory Management System (SQLite)

_Projects_

**Concepts:** `sqlite3` with several tables, foreign keys, transactions, low-stock alerts, sales reports with JOIN and GROUP BY.

Manage products and suppliers, record purchases and sales (which update the stock automatically) and get reports.

## Code

### Inventory Management  ([`main.py`](main.py))

```python
import sqlite3
import sys

DEMO = not sys.stdin.isatty()

SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY, sku TEXT UNIQUE, name TEXT, price REAL, stock INTEGER DEFAULT 0,
    reorder_level INTEGER DEFAULT 5);
CREATE TABLE IF NOT EXISTS movements (
    id INTEGER PRIMARY KEY, product_id INTEGER REFERENCES products(id), kind TEXT CHECK(kind IN ('IN','OUT')),
    qty INTEGER CHECK(qty > 0), unit_price REAL, ts TEXT DEFAULT CURRENT_TIMESTAMP);
"""

class Inventory:
    def __init__(self, db=":memory:"):
        self.conn = sqlite3.connect(db)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    def add_product(self, sku, name, price, reorder=5):
        with self.conn:
            self.conn.execute("INSERT INTO products (sku, name, price, reorder_level) VALUES (?,?,?,?)",
                              (sku, name, price, reorder))

    def _move(self, sku, kind, qty, price=None):
        p = self.conn.execute("SELECT * FROM products WHERE sku=?", (sku,)).fetchone()
        if p is None:
            raise KeyError(f"unknown SKU {sku}")
        if kind == "OUT" and p["stock"] < qty:
            raise ValueError(f"only {p['stock']} {p['name']} in stock")
        with self.conn:                                     # both statements or neither
            self.conn.execute("INSERT INTO movements (product_id, kind, qty, unit_price) VALUES (?,?,?,?)",
                              (p["id"], kind, qty, price or p["price"]))
            self.conn.execute("UPDATE products SET stock = stock + ? WHERE id=?",
                              (qty if kind == "IN" else -qty, p["id"]))

    def purchase(self, sku, qty, cost): self._move(sku, "IN", qty, cost)
    def sell(self, sku, qty): self._move(sku, "OUT", qty)

    def stock_report(self):
        print(f"\n{'SKU':<6}{'Product':<22}{'Stock':>6}{'Value':>11}  Status")
        for r in self.conn.execute("SELECT *, stock*price AS value FROM products ORDER BY name"):
            status = "⚠️ REORDER" if r["stock"] <= r["reorder_level"] else "ok"
            print(f"{r['sku']:<6}{r['name']:<22}{r['stock']:>6}{r['value']:>11,.2f}  {status}")

    def sales_report(self):
        q = """SELECT p.name, SUM(m.qty) qty, SUM(m.qty*m.unit_price) revenue
               FROM movements m JOIN products p ON p.id = m.product_id
               WHERE m.kind='OUT' GROUP BY p.id ORDER BY revenue DESC"""
        print("\n💰 Sales report")
        for r in self.conn.execute(q):
            print(f"   {r['name']:<22}{r['qty']:>5} sold   ₹{r['revenue']:>10,.2f}")
        total = self.conn.execute("SELECT COALESCE(SUM(qty*unit_price),0) FROM movements WHERE kind='OUT'").fetchone()[0]
        print(f"   {'TOTAL':<33}₹{total:>10,.2f}")

def main():
    inv = Inventory()
    for sku, name, price, reorder in [("A1", "USB-C Cable", 299, 10), ("A2", "Wireless Mouse", 799, 5),
                                      ("A3", "Mechanical Keyboard", 3499, 3), ("A4", "Arduino Uno", 650, 8)]:
        inv.add_product(sku, name, price, reorder)
    ops = [("purchase", "A1", 50, 180), ("purchase", "A2", 20, 500), ("purchase", "A3", 5, 2600),
           ("purchase", "A4", 15, 420), ("sell", "A1", 42), ("sell", "A2", 7), ("sell", "A3", 3),
           ("sell", "A4", 9), ("sell", "A3", 10), ("sell", "Z9", 1)]
    if not DEMO:
        print("Commands: purchase SKU QTY COST | sell SKU QTY | report | quit")
        ops = []
        while (line := input("> ").split()) and line[0] != "quit":
            if line[0] == "report":
                inv.stock_report(); inv.sales_report(); continue
            ops = [(line[0], line[1], *map(float, line[2:]))]
            for op in ops:
                try:
                    getattr(inv, op[0])(*op[1:])
                except (KeyError, ValueError) as e:
                    print("❌", e)
    for op in ops:
        try:
            getattr(inv, op[0])(*op[1:])
            print(f"✔ {op[0]:<8} {op[1]} x{op[2]}")
        except (KeyError, ValueError) as e:
            print(f"❌ {op[0]} {op[1]}: {e}")
    inv.stock_report()
    inv.sales_report()

if __name__ == "__main__":
    main()
```

## Extend this project

1. Add a suppliers table and generate automatic purchase orders for items low on stock.
2. Export the reports to Excel (openpyxl) or CSV.
3. Add a FastAPI or Flask web interface.

---

[⬅ Day 150](../Day-150-Project-Movie-Ticket-Booking-System/README.md) · [🏠 Home](../README.md) · [Day 152 ➡](../Day-152-Project-Smart-File-Organizer/README.md)
