# 028 · Raising Exceptions and Custom Exceptions — Example 1: raise for validation
# Run: python example_1.py

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"invalid age: {age}")
    return age

for value in [25, -5, "twenty"]:
    try:
        print("OK:", set_age(value))
    except (TypeError, ValueError) as e:
        print("Error:", e)
