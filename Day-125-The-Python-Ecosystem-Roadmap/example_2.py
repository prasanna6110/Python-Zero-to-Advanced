# Day 125 · The Python Ecosystem Roadmap — pandas-style data analysis (with a standard-library fallback)
# Run: python example_2.py

import csv, io, statistics
from collections import defaultdict

CSV = """name,dept,salary
Asha,EE,52000
Ravi,CS,61000
Meera,EE,58000
Kiran,CS,72000
Zoya,ME,49000
"""
try:
    import pandas as pd
    df = pd.read_csv(io.StringIO(CSV))
    print(df.groupby("dept")["salary"].agg(["mean", "max", "count"]))
except ImportError:
    print("pandas not installed -> pip install pandas. Using the standard library instead:")
    groups = defaultdict(list)
    for row in csv.DictReader(io.StringIO(CSV)):
        groups[row["dept"]].append(int(row["salary"]))
    print(f"{'dept':<5}{'mean':>10}{'max':>8}{'count':>7}")
    for dept, s in sorted(groups.items()):
        print(f"{dept:<5}{statistics.mean(s):>10.1f}{max(s):>8}{len(s):>7}")
