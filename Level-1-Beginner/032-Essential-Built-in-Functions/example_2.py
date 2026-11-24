# 032 · Essential Built-in Functions — Example 2: any, all, zip, enumerate
# Run: python example_2.py

marks = [45, 67, 89, 33]
print("Anyone failed?", any(m < 40 for m in marks))
print("All passed?", all(m >= 40 for m in marks))
names = ["A", "B", "C", "D"]
for i, (n, m) in enumerate(zip(names, marks), 1):
    print(i, n, m)
print(dict(zip(names, marks)))
