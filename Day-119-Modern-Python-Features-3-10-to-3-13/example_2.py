# Day 119 · Modern Python Features (3.10 to 3.13) — tomllib, new f-strings, batched and zip(strict)
# Run: python example_2.py

import tomllib
from itertools import batched

config = tomllib.loads('''
[app]
name = "Course Portal"
debug = true
[database]
port = 5432
hosts = ["db1", "db2"]
''')
print(config["app"]["name"], config["database"]["hosts"])

songs = ["a", "b"]
print(f"Songs: {", ".join(songs)}")             # PEP 701: reuse the same quotes (3.12+)
print(f"{'nested ' f'{1 + 1}'}")
print(list(batched(range(7), 3)))
try:
    list(zip([1, 2, 3], ["a", "b"], strict=True))
except ValueError as e:
    print("zip strict:", e)
