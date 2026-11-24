# Day 147 · Project: Expense Tracker with SQLite

_Projects_

**Concepts:** `sqlite3`, dataclasses, SQL aggregation (`GROUP BY`), transactions, budget checks, text bar charts.

Record your expenses by category, see where your money goes, and check whether you're within budget.

## Code

### Expense Tracker with SQLite  ([`main.py`](main.py))

```python
import sqlite3
from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    amount: float
    category: str
    note: str
    day: str = str(date(2026, 11, 24))

class ExpenseTracker:
    def __init__(self, db=":memory:"):
        self.conn = sqlite3.connect(db)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS expenses
            (id INTEGER PRIMARY KEY, amount REAL, category TEXT, note TEXT, day TEXT)""")

    def add(self, e: Expense):
        with self.conn:
            self.conn.execute("INSERT INTO expenses (amount, category, note, day) VALUES (?,?,?,?)",
                              (e.amount, e.category.lower(), e.note, e.day))

    def summary(self):
        return self.conn.execute("""SELECT category, COUNT(*), SUM(amount) FROM expenses
                                    GROUP BY category ORDER BY SUM(amount) DESC""").fetchall()

    def total(self):
        return self.conn.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses").fetchone()[0]

    def report(self, budget):
        print(f"{'Category':<12}{'Count':>6}{'Amount':>12}")
        print("-" * 30)
        for cat, n, amt in self.summary():
            bar = "█" * int(amt / self.total() * 20)
            print(f"{cat:<12}{n:>6}{amt:>12,.2f}  {bar}")
        spent = self.total()
        print("-" * 30)
        print(f"{'TOTAL':<18}{spent:>12,.2f}")
        status = "✅ within budget" if spent <= budget else f"⚠️ over budget by ₹{spent - budget:,.2f}"
        print(f"Budget ₹{budget:,} -> {status}")

tracker = ExpenseTracker()
for amt, cat, note in [(250, "Food", "mess extra"), (1200, "Books", "Micro-grids textbook"),
                       (90, "Travel", "auto"), (450, "Food", "birthday treat"), (60, "Travel", "bus")]:
    tracker.add(Expense(amt, cat, note))
tracker.report(budget=2000)
```

## Extend this project

1. Add a real argparse CLI: `add`, `report`, `export`.
2. Add monthly reports and CSV export.
3. Plot the categories with matplotlib.

---

[⬅ Day 146](../Day-146-Project-Python-Quiz-Engine/README.md) · [🏠 Home](../README.md) · [Day 148 ➡](../Day-148-Project-Library-Management-System/README.md)
