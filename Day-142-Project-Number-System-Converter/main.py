# Day 142 · Project: Number System Converter — Number System Converter
# Run: python main.py

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
