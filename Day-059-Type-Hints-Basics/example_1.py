# Day 059 · Type Hints Basics — Annotating functions
# Run: python example_1.py

def calculate_bmi(weight: float, height: float) -> float:
    return round(weight / height ** 2, 2)

def find_user(users: dict[int, str], uid: int) -> str | None:
    return users.get(uid)

print(calculate_bmi(70, 1.75))
print(find_user({1: "Asha"}, 1), find_user({1: "Asha"}, 2))
print(calculate_bmi.__annotations__)
