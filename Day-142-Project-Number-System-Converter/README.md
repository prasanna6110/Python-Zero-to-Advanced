# Day 142 · Project: Number System Converter

_Projects_

**Concepts:** base conversion algorithms, `int(x, base)`, `bin`/`oct`/`hex`, two's complement, input validation.

Convert between any bases from **2 to 36**, see the step-by-step division method, and view two's complement for negative numbers (great for digital electronics!).

## Code

### Number System Converter  ([`main.py`](main.py))

```python
import string
import sys

DEMO = not sys.stdin.isatty()
DIGITS = string.digits + string.ascii_uppercase

def to_base(n, base):
    if n == 0:
        return "0", []
    steps, digits, x = [], [], abs(n)
    while x > 0:
        x, r = divmod(x, base)
        steps.append(f"{x * base + r:>6} ÷ {base} = {x:<6} remainder {DIGITS[r]}")
        digits.append(DIGITS[r])
    return ("-" if n < 0 else "") + "".join(reversed(digits)), steps

def from_base(s, base):
    total = 0
    for ch in s.upper():
        v = DIGITS.index(ch)
        if v >= base:
            raise ValueError(f"digit {ch} is invalid in base {base}")
        total = total * base + v
    return total

def twos_complement(n, bits=8):
    return format(n & (2 ** bits - 1), f"0{bits}b")

def main():
    jobs = [("156", 10), ("FF", 16), ("101101", 2), ("Z", 36)] if DEMO else [(input("Number: "), int(input("Its base: ")))]
    for text, base in jobs:
        n = from_base(text, base)
        print(f"\n🔢 {text} (base {base}) = {n} (decimal)")
        for b, name in [(2, "Binary"), (8, "Octal"), (16, "Hex"), (36, "Base36")]:
            print(f"   {name:<7}: {to_base(n, b)[0]}")
    value, steps = to_base(156, 2)
    print("\nStep by step, 156 to binary:")
    print("\n".join("   " + s for s in steps), f"\n   read the remainders bottom-up -> {value}")
    print("\nTwo's complement (8-bit):", *(f"{x}={twos_complement(x)}" for x in [5, -5, -128, 127]))

if __name__ == "__main__":
    main()
```

## Extend this project

1. Add fractional numbers (0.625 in decimal is 0.101 in binary).
2. Add BCD and Gray code conversion.
3. Show IEEE-754 float bits using `struct`.

---

[⬅ Day 141](../Day-141-Project-Caesar-and-Vigenere-Cipher-Tool/README.md) · [🏠 Home](../README.md) · [Day 143 ➡](../Day-143-Project-Shopping-Bill-Generator-with-GST/README.md)
