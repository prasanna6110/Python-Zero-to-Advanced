# Day 006 · Numbers in Depth: int, float, Decimal, Fraction and complex — int and float behaviour
# Run: python example_1.py

big = 2 ** 200
print(big, "digits:", len(str(big)))
print(1_000_000 + 1, 7 // 2, -7 // 2, 7 % 3, -7 % 3)
print(0.1 + 0.2, 0.1 + 0.2 == 0.3)
import math
print(math.isclose(0.1 + 0.2, 0.3))
print(round(2.5), round(3.5), round(2.675, 2), "<- floats can surprise you")
print(float("inf") > 10 ** 100, float("nan") == float("nan"))
print((3.0).is_integer(), (255).bit_length())
