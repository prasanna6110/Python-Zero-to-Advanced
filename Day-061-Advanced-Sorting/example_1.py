# Day 061 · Advanced Sorting — Keys, multiple criteria and stability
# Run: python example_1.py

students = [("Ravi", "B", 82), ("Asha", "A", 95), ("Meera", "B", 82), ("Kiran", "A", 88)]
print(sorted(students, key=lambda s: s[2], reverse=True))
print(sorted(students, key=lambda s: (s[1], -s[2], s[0])))

# Stability: sort by the secondary key first, then by the primary key
step1 = sorted(students, key=lambda s: s[0])
step2 = sorted(step1, key=lambda s: s[1])
print(step2)
