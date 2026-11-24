# Day 102 · Working with Excel, PDF and Images (Popular Libraries) — Excel with openpyxl (CSV fallback)
# Run: python example_1.py

import csv, os

rows = [["Name", "Python", "Maths"], ["Asha", 91, 85], ["Ravi", 78, 92], ["Meera", 88, 79]]
try:
    from openpyxl import Workbook, load_workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Marks"
    for r in rows:
        ws.append(r)
    ws["D1"] = "Total"
    for i in range(2, len(rows) + 1):
        ws[f"D{i}"] = f"=B{i}+C{i}"            # a real Excel formula
    wb.save("marks.xlsx")
    ws2 = load_workbook("marks.xlsx").active
    print("Excel rows:", [[c.value for c in row] for row in ws2.iter_rows()])
    os.remove("marks.xlsx")
except ImportError:
    print("openpyxl not installed (pip install openpyxl). Writing a CSV instead:")
    with open("marks.csv", "w", newline="") as f:
        csv.writer(f).writerows([r + ["Total" if i == 0 else r[1] + r[2]] for i, r in enumerate(rows)])
    print(open("marks.csv").read())
    os.remove("marks.csv")
