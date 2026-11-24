# 059 · JSON and CSV — Example 1: JSON round trip
# Run: python example_1.py

import json

student = {"name": "Asha", "age": 21, "skills": ["python", "ml"], "hostel": True, "cgpa": None}
text = json.dumps(student, indent=2)
print(text)
back = json.loads(text)
print(back["skills"], type(back))

with open("student.json", "w") as f:
    json.dump(student, f)
with open("student.json") as f:
    print(json.load(f)["name"])
import os; os.remove("student.json")
