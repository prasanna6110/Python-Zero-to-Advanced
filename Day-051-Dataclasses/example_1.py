# Day 051 · Dataclasses — Basic dataclass
# Run: python example_1.py

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll: int
    cgpa: float = 0.0

s1 = Student("Asha", 101, 9.1)
s2 = Student("Asha", 101, 9.1)
print(s1)                 # automatic __repr__
print(s1 == s2)           # automatic __eq__
