# 053 · Walrus Operator, Unpacking and Star Expressions — Example 3: Star expressions for merging
# Run: python example_3.py

a, b = [1, 2], [3, 4]
print([*a, *b, 5])
print({*"hello", *"world"})
base = {"host": "localhost", "port": 8000}
prod = {**base, "host": "example.com", "debug": False}
print(prod)
print(*["x", "y", "z"], sep=" | ")
def show(a, b, c): return a + b + c
print(show(*[1, 2], **{"c": 3}))
