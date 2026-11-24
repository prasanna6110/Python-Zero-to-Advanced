# 021 · Tuples — Example 1: Basics
# Run: python example_1.py

t = (10, 20, 30, 20)
print(t[0], t[-1], t[1:3])
print(t.count(20), t.index(30))
single = (5,)
not_tuple = (5)
print(type(single), type(not_tuple))
# t[0] = 99 -> TypeError: tuples are immutable
