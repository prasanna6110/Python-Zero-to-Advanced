# Day 060 · Walrus Operator, Unpacking and Star Expressions — Walrus operator
# Run: python example_1.py

data = [5, 12, 7, 20, 3]
if (n := len(data)) > 3:
    print(f"List is long ({n} items)")

values = [1, 4, 9, 16, 25]
roots = [r for v in values if (r := v ** 0.5) > 2]
print(roots)

stream = iter(["a", "b", "", "c"])
while (item := next(stream)) != "":
    print("read", item)
