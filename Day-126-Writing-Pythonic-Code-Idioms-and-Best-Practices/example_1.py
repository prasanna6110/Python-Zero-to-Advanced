# Day 126 · Writing Pythonic Code (Idioms and Best Practices) — Before and after: Pythonic rewrites
# Run: python example_1.py

names = ["asha", "ravi", "meera"]
marks = [91, 78, 88]

# Non-Pythonic
result = []
for i in range(len(names)):
    if marks[i] > 80:
        result.append(names[i].upper())
print(result)

# Pythonic
print([n.upper() for n, m in zip(names, marks) if m > 80])

# Non-Pythonic
found = False
for n in names:
    if n == "ravi":
        found = True
# Pythonic
found = "ravi" in names
print(found, "| any above 90:", any(m > 90 for m in marks))
