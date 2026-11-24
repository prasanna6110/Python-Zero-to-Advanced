# 025 · Mutable vs Immutable and Copying — Example 1: Immutable creates new objects
# Run: python example_1.py

s = "hi"
print(id(s))
s += "!"
print(id(s), "(new object)")
lst = [1, 2]
print(id(lst))
lst += [3]
print(id(lst), "(same object, changed in place)")
