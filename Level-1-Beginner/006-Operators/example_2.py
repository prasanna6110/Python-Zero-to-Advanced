# 006 · Operators — Example 2: Comparison, logical, identity, membership
# Run: python example_2.py

x = 15
print(10 < x < 20)                 # chained comparison
print(x > 10 and x % 2 == 0)
print(not x == 15)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)              # same value, different objects
print(2 in a, 5 not in a)
print("" or "default")             # 'or' returns the first truthy value
