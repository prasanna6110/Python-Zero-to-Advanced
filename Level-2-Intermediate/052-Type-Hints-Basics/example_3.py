# 052 · Type Hints Basics — Example 3: Hints are not enforced at runtime
# Run: python example_3.py

def double(x: int) -> int:
    return x * 2

print(double(5))
print(double("ha"))     # works! Python doesn't check, but mypy would flag it

import typing
print(typing.get_type_hints(double))
