# 053 · Walrus Operator, Unpacking and Star Expressions — Example 2: Extended and nested unpacking
# Run: python example_2.py

first, *middle, last = range(1, 8)
print(first, middle, last)

*_, final = "python"
print(final)

record = ("Asha", (21, "EE"), [9.1, 8.7])
name, (age, branch), [sem1, sem2] = record
print(name, age, branch, sem1, sem2)

for i, (k, v) in enumerate({"a": 1, "b": 2}.items()):
    print(i, k, v)
