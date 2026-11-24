# Day 006 · Numbers in Depth: int, float, Decimal, Fraction and complex — Decimal for money and Fraction for exact maths
# Run: python example_2.py

from decimal import Decimal, ROUND_HALF_UP, getcontext
from fractions import Fraction

price = Decimal("19.99")
qty = 3
gst = Decimal("0.18")
total = price * qty * (1 + gst)
print("Total:", total, "->", total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
print(Decimal(0.1), "<- created from a float (bad)")
print(Decimal("0.1"), "<- created from a string (good)")
getcontext().prec = 50
print(Decimal(1) / Decimal(7))

f = Fraction(1, 3) + Fraction(1, 6)
print(f, float(f), Fraction("0.75"), Fraction(3, 4) * 2)
