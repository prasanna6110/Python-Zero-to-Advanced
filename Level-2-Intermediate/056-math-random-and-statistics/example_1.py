# 056 · math, random and statistics — Example 1: math functions
# Run: python example_1.py

import math

print(math.sqrt(144), math.floor(3.7), math.ceil(3.2), math.trunc(-3.7))
print(math.factorial(6), math.gcd(48, 36), math.lcm(4, 6))
print(math.comb(5, 2), math.perm(5, 2))         # nCr, nPr
print(math.log(100, 10), math.log2(1024), math.exp(1))
print(math.sin(math.radians(30)), math.hypot(3, 4))
print(0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))
