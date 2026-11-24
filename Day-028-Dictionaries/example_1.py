# Day 028 · Dictionaries — CRUD on a dictionary
# Run: python example_1.py

student = {"name": "Asha", "age": 21}
student["branch"] = "EE"           # create
print(student["name"])             # read
student["age"] = 22                # update
del student["branch"]              # delete
print(student)
print(student.get("cgpa", "N/A"))  # safe read
