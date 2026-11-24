# 033 · Lambda Functions — Example 2: Sorting with lambda keys
# Run: python example_2.py

students = [
    {"name": "Asha", "cgpa": 8.9, "age": 21},
    {"name": "Ravi", "cgpa": 9.4, "age": 22},
    {"name": "Meera", "cgpa": 8.9, "age": 20},
]
by_cgpa = sorted(students, key=lambda s: (-s["cgpa"], s["name"]))
for s in by_cgpa:
    print(s["name"], s["cgpa"])
print(min(students, key=lambda s: s["age"])["name"])
