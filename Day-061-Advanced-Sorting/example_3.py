# Day 061 · Advanced Sorting — cmp_to_key and natural sort
# Run: python example_3.py

from functools import cmp_to_key
import re

def largest_number(nums):
    """Arrange numbers so they form the largest possible number."""
    def cmp(a, b):
        return -1 if a + b > b + a else (1 if a + b < b + a else 0)
    return "".join(sorted(map(str, nums), key=cmp_to_key(cmp)))

print(largest_number([3, 30, 34, 5, 9]))

files = ["file10.txt", "file2.txt", "file1.txt"]
natural = lambda s: [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]
print(sorted(files), "vs", sorted(files, key=natural))
