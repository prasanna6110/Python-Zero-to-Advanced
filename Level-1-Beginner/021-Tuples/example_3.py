# 021 · Tuples — Example 3: Tuples as dictionary keys
# Run: python example_3.py

distances = {
    ("Delhi", "Kurukshetra"): 160,
    ("Delhi", "Agra"): 230,
}
print(distances[("Delhi", "Agra")])

students = [("Asha", 91), ("Vikram", 85), ("Zoya", 97)]
for name, mark in sorted(students, key=lambda s: s[1], reverse=True):
    print(name, mark)
