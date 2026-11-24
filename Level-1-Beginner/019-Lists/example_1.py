# 019 · Lists — Example 1: Creating and accessing
# Run: python example_1.py

fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0], fruits[-1])
print(fruits[1:3])
fruits[1] = "blueberry"
print(fruits)
print("cherry" in fruits, len(fruits))
