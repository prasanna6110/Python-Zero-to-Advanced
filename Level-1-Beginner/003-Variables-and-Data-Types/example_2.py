# 003 · Variables and Data Types — Example 2: Multiple assignment and swapping
# Run: python example_2.py

a, b, c = 1, 2, 3
print(a, b, c)

x = y = z = 0          # same value to many variables
print(x, y, z)

a, b = b, a            # swap without a temporary variable
print("After swap:", a, b)
