# Day 139 · Project: Student Report Card System

_Projects_

**Concepts:** dictionaries of lists, statistics, grading rules, ranking, formatted tables, file export.

Enter the marks for several students and subjects. The program calculates totals, percentages, grades, SGPA-style points, ranks and class toppers, then exports a report.

## Code

### Student Report Card  ([`main.py`](main.py))

```python
import statistics
import sys

DEMO = not sys.stdin.isatty()
SUBJECTS = ["Python", "Micro-Grids", "Power Systems", "Maths"]
GRADES = [(90, "O", 10), (80, "A+", 9), (70, "A", 8), (60, "B+", 7), (50, "B", 6), (40, "C", 5), (0, "F", 0)]

def grade_for(mark):
    return next((g, p) for cutoff, g, p in GRADES if mark >= cutoff)

def collect():
    if DEMO:
        return {
            "Asha": [92, 85, 78, 88], "Ravi": [67, 74, 81, 59], "Meera": [88, 91, 95, 84],
            "Kiran": [45, 38, 52, 61], "Zoya": [79, 82, 70, 90],
        }
    students = {}
    n = int(input("Number of students: "))
    for _ in range(n):
        name = input("\nStudent name: ").strip().title()
        students[name] = [float(input(f"  {s} marks (0-100): ")) for s in SUBJECTS]
    return students

def report(students):
    rows = []
    for name, marks in students.items():
        total = sum(marks)
        pct = total / len(marks)
        points = [grade_for(m)[1] for m in marks]
        failed = any(p == 0 for p in points)
        rows.append({"name": name, "marks": marks, "total": total, "pct": pct,
                     "grade": grade_for(pct)[0], "sgpa": sum(points) / len(points), "result": "FAIL" if failed else "PASS"})
    rows.sort(key=lambda r: r["total"], reverse=True)
    header = f"{'Rank':<5}{'Name':<8}" + "".join(f"{s[:8]:>9}" for s in SUBJECTS) + f"{'Total':>7}{'%':>7}{'Grd':>5}{'SGPA':>6}  Result"
    lines = [header, "-" * len(header)]
    for rank, r in enumerate(rows, 1):
        lines.append(f"{rank:<5}{r['name']:<8}" + "".join(f"{m:>9.0f}" for m in r["marks"])
                     + f"{r['total']:>7.0f}{r['pct']:>7.1f}{r['grade']:>5}{r['sgpa']:>6.2f}  {r['result']}")
    lines.append("")
    for i, s in enumerate(SUBJECTS):
        col = [r["marks"][i] for r in rows]
        top = max(rows, key=lambda r: r["marks"][i])["name"]
        lines.append(f"{s:<14} avg {statistics.mean(col):5.1f} | highest {max(col):3.0f} ({top}) | std {statistics.stdev(col):4.1f}")
    lines.append(f"\n🏆 Class topper: {rows[0]['name']} ({rows[0]['pct']:.1f}%)")
    lines.append(f"Pass rate: {sum(r['result'] == 'PASS' for r in rows) / len(rows):.0%}")
    return "\n".join(lines)

if __name__ == "__main__":
    text = report(collect())
    print(text)
    if not DEMO:
        with open("report_card.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("\nSaved to report_card.txt")
```

## Extend this project

1. Read the marks from a CSV file.
2. Add a bar chart of percentages (matplotlib or a text chart).
3. Generate a separate report card file for each student.

---

[⬅ Day 138](../Day-138-Project-Contact-Book-CSV-with-Search-and-Validation/README.md) · [🏠 Home](../README.md) · [Day 140 ➡](../Day-140-Project-Text-Analyzer/README.md)
