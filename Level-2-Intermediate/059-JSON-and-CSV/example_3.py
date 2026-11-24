# 059 · JSON and CSV — Example 3: CSV with DictWriter and DictReader
# Run: python example_3.py

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
