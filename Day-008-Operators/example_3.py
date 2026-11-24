# Day 008 · Operators — Bitwise operators
# Run: python example_3.py

a, b = 12, 10          # 1100, 1010
print(f"a & b  = {a & b}  ({a & b:04b})")
print(f"a | b  = {a | b} ({a | b:04b})")
print(f"a ^ b  = {a ^ b}  ({a ^ b:04b})")
print(f"a << 1 = {a << 1}")
print(f"a >> 2 = {a >> 2}")
n = 7
print("Is 7 odd?", bool(n & 1))   # fast odd/even check
