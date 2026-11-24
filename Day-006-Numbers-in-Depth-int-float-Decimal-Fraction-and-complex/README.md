# Day 006 · Numbers in Depth: int, float, Decimal, Fraction and complex

_Beginner_

## int
Python integers have **unlimited size**, so `2 ** 1000` works fine. You can write `1_000_000` to make big numbers readable.

## float
Floats are 64-bit (IEEE 754), so they have **rounding errors**: `0.1 + 0.2 != 0.3`.
- Compare floats with `math.isclose(a, b)`.
- `round(x, 2)` uses banker's rounding: `round(2.5) == 2`.
- Special values: `float("inf")`, `float("nan")`.

## Decimal: exact decimal arithmetic (for money!)
`from decimal import Decimal`, then `Decimal("0.1") + Decimal("0.2") == Decimal("0.3")`.
Always create a Decimal from a **string**, not from a float.

## Fraction: exact fractions
`Fraction(1, 3) + Fraction(1, 6)` gives `Fraction(1, 2)`.

## complex
`3 + 4j` has `.real`, `.imag`, `abs()` and `.conjugate()`. The `cmath` module has maths functions for complex numbers. They're very useful in electrical engineering, for things like AC phasors.

## Useful functions
`abs, round, divmod, pow(a, b, mod), int(x, base), bin/oct/hex, math.floor/ceil/trunc, float.is_integer(), int.bit_length()`

## Examples

### Example 1: int and float behaviour  ([`example_1.py`](example_1.py))

```python
big = 2 ** 200
print(big, "digits:", len(str(big)))
print(1_000_000 + 1, 7 // 2, -7 // 2, 7 % 3, -7 % 3)
print(0.1 + 0.2, 0.1 + 0.2 == 0.3)
import math
print(math.isclose(0.1 + 0.2, 0.3))
print(round(2.5), round(3.5), round(2.675, 2), "<- floats can surprise you")
print(float("inf") > 10 ** 100, float("nan") == float("nan"))
print((3.0).is_integer(), (255).bit_length())
```

### Example 2: Decimal for money and Fraction for exact maths  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: complex numbers: AC circuit phasors  ([`example_3.py`](example_3.py))

```python
import cmath, math

V = 230 * cmath.exp(1j * 0)           # 230 V at 0°
Z = complex(10, 5)                    # R = 10 Ω, X_L = 5 Ω
I = V / Z
print(f"Impedance |Z| = {abs(Z):.2f} Ω at {math.degrees(cmath.phase(Z)):.2f}°")
print(f"Current   |I| = {abs(I):.2f} A at {math.degrees(cmath.phase(I)):.2f}°")
S = V * I.conjugate()
print(f"Real power P = {S.real:.1f} W, reactive Q = {S.imag:.1f} VAR, pf = {S.real / abs(S):.3f}")
print(cmath.sqrt(-16), (3 + 4j).real, (3 + 4j).imag, abs(3 + 4j))
```

## Practice

1. Calculate the simple and compound interest on ₹10,000 using Decimal.
2. Add 1/2 + 1/3 + 1/4 using Fraction.
3. Calculate the power factor of a load with R = 8 Ω and X = 6 Ω.

---

[⬅ Day 005](../Day-005-Type-Casting/README.md) · [🏠 Home](../README.md) · [Day 007 ➡](../Day-007-Taking-User-Input/README.md)
