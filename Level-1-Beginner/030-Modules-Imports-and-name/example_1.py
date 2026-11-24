# 030 · Modules, Imports and __name__ — Example 1: Different import styles
# Run: python example_1.py

import math
import random as rnd
from datetime import date
from statistics import mean, median

print(math.pi, math.factorial(5))
rnd.seed(1)
print(rnd.randint(1, 100))
print(date(2026, 1, 13).strftime("%A"))
print(mean([1, 2, 3, 4]), median([5, 1, 9]))
