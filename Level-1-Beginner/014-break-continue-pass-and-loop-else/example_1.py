# 014 · break, continue, pass and loop-else — Example 1: break and continue
# Run: python example_1.py

for n in range(1, 11):
    if n == 8:
        break          # stop completely at 8
    if n % 2 == 0:
        continue       # skip even numbers
    print(n)
