# 022 · Sets — Example 2: Set operations
# Run: python example_2.py

python_students = {"Amit", "Riya", "Karan", "Neha"}
java_students = {"Riya", "Neha", "Sam"}
print("Both:", python_students & java_students)
print("Either:", python_students | java_students)
print("Only Python:", python_students - java_students)
print("Exactly one:", python_students ^ java_students)
print({"Riya"} <= java_students)
