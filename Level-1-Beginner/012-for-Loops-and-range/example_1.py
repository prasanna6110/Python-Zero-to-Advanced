# 012 · for Loops and range() — Example 1: Looping over different things
# Run: python example_1.py

for ch in "abc":
    print(ch, end=" ")
print()
for fruit in ["apple", "mango", "kiwi"]:
    print(fruit.upper())
for i in range(1, 11, 3):
    print(i, end=" ")
print()
student = {"name": "Riya", "branch": "EE"}
for key, value in student.items():
    print(key, "=", value)
