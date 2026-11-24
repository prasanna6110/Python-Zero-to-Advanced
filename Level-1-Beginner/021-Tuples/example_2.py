# 021 · Tuples — Example 2: Unpacking
# Run: python example_2.py

point = (3, 4)
x, y = point
print(f"x={x}, y={y}")

first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)

def min_max(lst):
    return min(lst), max(lst)     # returns a tuple
lo, hi = min_max([5, 2, 9])
print(lo, hi)
