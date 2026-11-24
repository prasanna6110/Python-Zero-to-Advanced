# 026 · Docstrings and PEP 8 (Writing Clean Code) — Example 1: Writing and reading docstrings
# Run: python example_1.py

def bmi(weight_kg, height_m):
    """Calculate Body Mass Index.

    Args:
        weight_kg: weight in kilograms
        height_m: height in metres

    Returns:
        BMI rounded to 1 decimal place.
    """
    return round(weight_kg / height_m ** 2, 1)

print(bmi(70, 1.75))
print(bmi.__doc__)
