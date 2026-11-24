# Day 148 · Project: Library Management System — Library Management System
# Run: python main.py

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
