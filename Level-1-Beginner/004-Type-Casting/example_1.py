# 004 · Type Casting — Example 1: Implicit vs explicit conversion
# Run: python example_1.py

a = 5          # int
b = 2.5        # float
print(a + b, type(a + b))   # implicit: int -> float

num_str = "100"
print(int(num_str) + 50)    # explicit: str -> int
print(str(50) + "%")        # explicit: int -> str
