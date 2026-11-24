# Day 012 · Conditional Statements: if, elif, else — Grade calculator
# Run: python example_1.py

marks = 78
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"
print(f"Marks: {marks}, Grade: {grade}")
