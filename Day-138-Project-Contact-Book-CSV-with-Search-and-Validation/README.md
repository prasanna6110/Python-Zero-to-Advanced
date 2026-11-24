# Day 138 · Project: Contact Book (CSV with Search and Validation)

_Projects_

**Concepts:** `csv.DictReader`/`DictWriter`, regex validation, searching, sorting, classes.

Store contacts with a validated phone number and email address. Search by any field, and export to vCard format.

## Code

### Contact Book  ([`main.py`](main.py))

```python
import csv
import re
import sys
from pathlib import Path

DEMO = not sys.stdin.isatty()
FILE = Path("contacts_demo.csv" if DEMO else "contacts.csv")
FIELDS = ["name", "phone", "email", "city"]
DEMO_INPUTS = iter(["1", "Asha Verma", "9876543210", "asha@mail.com", "Delhi",
                    "1", "Ravi Kumar", "12345", "9123456780", "ravi@", "ravi@mail.com", "Kurukshetra",
                    "1", "Meera Iyer", "8899776655", "meera@mail.in", "Chennai",
                    "2", "3", "ku", "5", "4", "Ravi Kumar", "2", "0"])

def ask(prompt):
    if DEMO:
        v = next(DEMO_INPUTS); print(prompt + v); return v
    return input(prompt)

def ask_valid(prompt, pattern, error):
    while True:
        value = ask(prompt).strip()
        if re.fullmatch(pattern, value):
            return value
        print("  ❌", error)

class ContactBook:
    def __init__(self, path):
        self.path = path
        self.contacts = list(csv.DictReader(path.open())) if path.exists() else []
    def save(self):
        with self.path.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(self.contacts)
    def add(self, c):
        self.contacts.append(c); self.save()
    def search(self, q):
        q = q.lower()
        return [c for c in self.contacts if any(q in c[k].lower() for k in FIELDS)]
    def delete(self, name):
        before = len(self.contacts)
        self.contacts = [c for c in self.contacts if c["name"].lower() != name.lower()]
        self.save()
        return before - len(self.contacts)
    def vcard(self, c):
        return f"BEGIN:VCARD\nVERSION:3.0\nFN:{c['name']}\nTEL:{c['phone']}\nEMAIL:{c['email']}\nEND:VCARD"

def show(contacts):
    print(f"  {'Name':<14}{'Phone':<13}{'Email':<18}City")
    for c in sorted(contacts, key=lambda c: c["name"]):
        print(f"  {c['name']:<14}{c['phone']:<13}{c['email']:<18}{c['city']}")

def main():
    book = ContactBook(FILE)
    while True:
        print("\n📒 1.Add 2.List 3.Search 4.Delete 5.Export vCard 0.Exit")
        c = ask("> ")
        if c == "1":
            book.add({
                "name": ask("Name: ").strip().title(),
                "phone": ask_valid("Phone (10 digits): ", r"[6-9]\d{9}", "Indian mobile: 10 digits starting 6-9"),
                "email": ask_valid("Email: ", r"[\w.+-]+@[\w-]+\.[\w.]+", "Invalid email"),
                "city": ask("City: ").strip(),
            })
        elif c == "2":
            show(book.contacts)
        elif c == "3":
            show(book.search(ask("Search: ")))
        elif c == "4":
            print("Deleted", book.delete(ask("Exact name: ")), "contact(s)")
        elif c == "5":
            print("\n\n".join(book.vcard(x) for x in book.contacts[:1]), "\n(...)")
        elif c == "0":
            break
    if DEMO:
        FILE.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
```

## Extend this project

1. Prevent duplicate phone numbers.
2. Add birthdays, and show the upcoming ones this month.
3. Import contacts from a vCard (`.vcf`) file.

---

[⬅ Day 137](../Day-137-Project-To-Do-List-Manager-JSON-Storage/README.md) · [🏠 Home](../README.md) · [Day 139 ➡](../Day-139-Project-Student-Report-Card-System/README.md)
