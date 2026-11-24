# Day 068 · JSON and CSV

_Intermediate_

## JSON (JavaScript Object Notation)
The most common format for APIs and config files.
| Function | Purpose |
|----------|---------|
| `json.dumps(obj, indent=2)` | Python object → JSON string |
| `json.loads(text)` | JSON string → Python object |
| `json.dump(obj, file)` / `json.load(file)` | work with files |

Mapping: dict ↔ object, list ↔ array, str, int/float, True ↔ true, None ↔ null.

To save custom objects, pass `default=` (or subclass `JSONEncoder`).

## CSV
- `csv.reader` / `csv.writer` work with rows as lists.
- `csv.DictReader` / `csv.DictWriter` work with rows as dicts (recommended).
- Always open CSV files with `newline=""`.

## Examples

### Example 1: JSON round trip  ([`example_1.py`](example_1.py))

```python
import json

student = {"name": "Asha", "age": 21, "skills": ["python", "ml"], "hostel": True, "cgpa": None}
text = json.dumps(student, indent=2)
print(text)
back = json.loads(text)
print(back["skills"], type(back))

with open("student.json", "w") as f:
    json.dump(student, f)
with open("student.json") as f:
    print(json.load(f)["name"])
import os; os.remove("student.json")
```

### Example 2: Serialising custom objects  ([`example_2.py`](example_2.py))

```python
import json
from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class Event:
    title: str
    day: date

def encoder(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Can't serialise {type(obj)}")

events = [Event("Mid-term", date(2026, 11, 28)), Event("Project demo", date(2026, 12, 5))]
payload = json.dumps([asdict(e) for e in events], default=encoder, indent=1)
print(payload)
loaded = [Event(d["title"], date.fromisoformat(d["day"])) for d in json.loads(payload)]
print(loaded[0])
```

### Example 3: CSV with DictWriter and DictReader  ([`example_3.py`](example_3.py))

```python
import csv, os

rows = [
    {"name": "Asha", "dept": "EE", "salary": 52000},
    {"name": "Ravi", "dept": "CS", "salary": 61000},
    {"name": "Meera", "dept": "EE", "salary": 58000},
]
with open("employees.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "dept", "salary"])
    writer.writeheader()
    writer.writerows(rows)

dept_total = {}
with open("employees.csv", newline="") as f:
    for row in csv.DictReader(f):
        dept_total[row["dept"]] = dept_total.get(row["dept"], 0) + int(row["salary"])
print(dept_total)
os.remove("employees.csv")
```

## Practice

1. Save a contact book to a JSON file and load it back.
2. Read a CSV of marks and write a new CSV with an added "grade" column.
3. Convert a CSV file to JSON.

---

[⬅ Day 067](../Day-067-sys-and-argparse-Command-Line-Programs/README.md) · [🏠 Home](../README.md) · [Day 069 ➡](../Day-069-Regular-Expressions-re/README.md)
