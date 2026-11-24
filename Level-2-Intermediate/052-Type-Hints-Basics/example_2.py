# 052 · Type Hints Basics — Example 2: Collections, Callable and type aliases
# Run: python example_2.py

from collections.abc import Callable

Matrix = list[list[float]]          # type alias

def apply(func: Callable[[int], int], values: list[int]) -> list[int]:
    return [func(v) for v in values]

def identity(n: int) -> Matrix:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

print(apply(lambda x: x * 10, [1, 2, 3]))
print(identity(3))
