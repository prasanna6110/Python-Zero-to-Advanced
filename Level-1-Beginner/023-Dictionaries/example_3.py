# 023 · Dictionaries — Example 3: Nested dicts, merging and iterating
# Run: python example_3.py

db = {
    "u1": {"name": "Ravi", "skills": ["python", "sql"]},
    "u2": {"name": "Meera", "skills": ["java"]},
}
db["u2"]["skills"].append("python")
for uid, info in db.items():
    print(uid, info["name"], ", ".join(info["skills"]))

defaults = {"theme": "light", "lang": "en"}
user_prefs = {"theme": "dark"}
print(defaults | user_prefs)       # Python 3.9+ merge
print(dict.fromkeys(["a", "b"], 0))
