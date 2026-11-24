# 106 · Modern Python Features (3.10 to 3.13) — Example 1: ExceptionGroup, except* and add_note
# Run: python example_1.py

def validate(user):
    errors = []
    if not user.get("name"):
        errors.append(ValueError("name is required"))
    if user.get("age", 0) < 0:
        errors.append(ValueError("age must be positive"))
    if "@" not in user.get("email", ""):
        errors.append(TypeError("email is malformed"))
    if errors:
        raise ExceptionGroup("invalid user", errors)

try:
    validate({"name": "", "age": -2, "email": "nope"})
except* ValueError as eg:
    print("Value errors:", [str(e) for e in eg.exceptions])
except* TypeError as eg:
    print("Type errors:", [str(e) for e in eg.exceptions])

try:
    int("abc")
except ValueError as e:
    e.add_note("Hint: the input came from config.toml line 3")
    print(e, "| notes:", e.__notes__)
