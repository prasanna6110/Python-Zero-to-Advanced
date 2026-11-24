# Day 061 · Advanced Sorting — itemgetter and attrgetter
# Run: python example_2.py

from operator import itemgetter, attrgetter
from dataclasses import dataclass

rows = [{"name": "Zed", "age": 30}, {"name": "Amy", "age": 25}, {"name": "Bob", "age": 30}]
print(sorted(rows, key=itemgetter("age", "name")))

@dataclass
class Emp:
    name: str
    salary: int

emps = [Emp("A", 300), Emp("B", 100), Emp("C", 200)]
print([e.name for e in sorted(emps, key=attrgetter("salary"))])
print(max(emps, key=attrgetter("salary")))
