# 004 · Type Casting — Example 2: Truthy and falsy values
# Run: python example_2.py

for value in [0, 1, -5, 0.0, "", "0", [], [0], None, {}]:
    print(f"bool({value!r}) = {bool(value)}")
