# Day 024 · Lists — Reference vs copy
# Run: python example_3.py

a = [1, 2, 3]
b = a           # same object
c = a.copy()    # new object
b.append(4)
print("a:", a)
print("b:", b)
print("c:", c)
print(a is b, a is c)
