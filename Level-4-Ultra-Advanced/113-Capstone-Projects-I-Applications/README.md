# 113 · Capstone Projects I: Applications

## Put it all together
These projects combine many topics from the course. Read the code, run it, then **extend it**.

| Project | Concepts used |
|---------|---------------|
| 1. Expense Tracker | sqlite3, dataclasses, argparse-style commands, f-strings, aggregation |
| 2. Library Management System | OOP, inheritance, custom exceptions, JSON persistence, Enum |
| 3. Quiz Engine | JSON data, random, closures, a scoring strategy, a type-hinted API |

Each project runs automatically using sample commands. Change it to take real `input()` or command-line arguments.

## Examples

### Example 1: Expense Tracker (sqlite3 + dataclasses)  ([`example_1.py`](example_1.py))

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

### Example 2: Library Management System (OOP + JSON + custom exceptions)  ([`example_2.py`](example_2.py))

```python
import json
from enum import Enum
from datetime import date, timedelta

class LibraryError(Exception): pass
class NotAvailable(LibraryError): pass
class LimitReached(LibraryError): pass

class Status(Enum):
    AVAILABLE = "available"
    ISSUED = "issued"

class Book:
    def __init__(self, isbn, title, author, status=Status.AVAILABLE):
        self.isbn, self.title, self.author, self.status = isbn, title, author, Status(status)
    def to_dict(self):
        return {"isbn": self.isbn, "title": self.title, "author": self.author, "status": self.status.value}

class Member:
    LIMIT = 2
    def __init__(self, mid, name):
        self.mid, self.name, self.books = mid, name, {}

class Faculty(Member):
    LIMIT = 5

class Library:
    FINE_PER_DAY = 5
    def __init__(self):
        self.books, self.members = {}, {}
    def add_book(self, book): self.books[book.isbn] = book
    def join(self, member): self.members[member.mid] = member
    def issue(self, isbn, mid, today):
        book, m = self.books[isbn], self.members[mid]
        if book.status is Status.ISSUED: raise NotAvailable(f"'{book.title}' is already issued")
        if len(m.books) >= m.LIMIT: raise LimitReached(f"{m.name} reached the limit of {m.LIMIT}")
        book.status = Status.ISSUED
        m.books[isbn] = today + timedelta(days=14)
        print(f"Issued '{book.title}' to {m.name}, due {m.books[isbn]}")
    def give_back(self, isbn, mid, today):
        m = self.members[mid]
        due = m.books.pop(isbn)
        self.books[isbn].status = Status.AVAILABLE
        fine = max(0, (today - due).days) * self.FINE_PER_DAY
        print(f"{m.name} returned '{self.books[isbn].title}'. Fine: ₹{fine}")
    def save(self):
        return json.dumps([b.to_dict() for b in self.books.values()], indent=1)

lib = Library()
for b in [Book("111", "Python Deep Dive", "Author A"), Book("222", "Writing Clean Code", "Author B"),
          Book("333", "Power System Analysis", "Author C")]:
    lib.add_book(b)
lib.join(Member("S1", "Asha")); lib.join(Faculty("F1", "Dr. Verma"))
d0 = date(2026, 11, 1)
lib.issue("111", "S1", d0)
lib.issue("222", "S1", d0)
for action in [lambda: lib.issue("333", "S1", d0), lambda: lib.issue("111", "F1", d0)]:
    try:
        action()
    except LibraryError as e:
        print(f"{type(e).__name__}: {e}")
lib.give_back("111", "S1", d0 + timedelta(days=20))
print("Saved state:", lib.save())
```

### Example 3: Quiz Engine (JSON data + closures + strategies)  ([`example_3.py`](example_3.py))

```python
import json, random
from typing import Callable

QUESTIONS_JSON = """[
 {"q": "Output of len({1, 1, 2})?", "options": ["1", "2", "3"], "answer": "2", "level": 1},
 {"q": "Which keyword makes a generator?", "options": ["return", "yield", "async"], "answer": "yield", "level": 1},
 {"q": "Default metaclass of every class?", "options": ["object", "type", "ABCMeta"], "answer": "type", "level": 3},
 {"q": "What does the GIL limit?", "options": ["I/O", "Parallel bytecode execution", "Memory"], "answer": "Parallel bytecode execution", "level": 3},
 {"q": "Which module do asyncio's selectors build on?", "options": ["selectors", "socketserver", "ssl"], "answer": "selectors", "level": 4}
]"""

def make_scorer(strategy: str) -> Callable[[dict, bool], int]:
    streak = 0
    def flat(q, correct): return 1 if correct else 0
    def weighted(q, correct): return q["level"] if correct else 0
    def streak_bonus(q, correct):
        nonlocal streak
        streak = streak + 1 if correct else 0
        return streak if correct else 0
    return {"flat": flat, "weighted": weighted, "streak": streak_bonus}[strategy]

def run_quiz(questions, answer_fn, strategy="weighted"):
    score_fn, score = make_scorer(strategy), 0
    for i, q in enumerate(questions, 1):
        opts = q["options"][:]
        random.shuffle(opts)
        choice = answer_fn(q, opts)
        correct = choice == q["answer"]
        score += score_fn(q, correct)
        print(f"Q{i}. {q['q']}\n    options: {opts}\n    you: {choice} -> {'✅' if correct else '❌ ' + q['answer']}")
    return score

random.seed(5)
questions = json.loads(QUESTIONS_JSON)
smart_player = lambda q, opts: q["answer"] if q["level"] < 4 else opts[0]   # simulates the user's answers
for strategy in ["flat", "weighted", "streak"]:
    print(f"\n=== strategy: {strategy} ===")
    print("FINAL SCORE:", run_quiz(questions, smart_player, strategy))
```

## Practice

1. Expense tracker: add monthly reports and CSV export, plus a real argparse CLI.
2. Library: save and load members too, and add search by author.
3. Quiz: read real answers with `input()`, add a timer and store high scores in a JSON file.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
