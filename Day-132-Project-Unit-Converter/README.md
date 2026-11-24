# Day 132 · Project: Unit Converter

_Projects_

**Concepts:** nested dictionaries, conversion factors, functions, formatted tables.

It converts **length, weight, temperature, data size, speed and energy**. Temperature needs formulas rather than factors, so it's handled separately.

## Code

### Unit Converter  ([`main.py`](main.py))

```python
import sys

DEMO = not sys.stdin.isatty()
DEMO_INPUTS = iter(["length", "5", "km", "mi", "temperature", "36.6", "C", "F", "data", "2", "GB", "MB", "q"])

def ask(prompt):
    if DEMO:
        v = next(DEMO_INPUTS); print(prompt + v); return v
    return input(prompt)

# factor to convert 1 unit -> base unit
UNITS = {
    "length": {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254, "ft": 0.3048, "mi": 1609.344},
    "weight": {"mg": 1e-6, "g": 0.001, "kg": 1, "lb": 0.453592, "oz": 0.0283495, "ton": 1000},
    "data": {"B": 1, "KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3, "TB": 1024 ** 4},
    "speed": {"m/s": 1, "km/h": 1 / 3.6, "mph": 0.44704, "knot": 0.514444},
    "energy": {"J": 1, "kJ": 1000, "kWh": 3.6e6, "cal": 4.184, "kcal": 4184},
}

def convert_temperature(value, src, dst):
    to_c = {"C": lambda v: v, "F": lambda v: (v - 32) * 5 / 9, "K": lambda v: v - 273.15}
    from_c = {"C": lambda v: v, "F": lambda v: v * 9 / 5 + 32, "K": lambda v: v + 273.15}
    return from_c[dst](to_c[src](value))

def convert(category, value, src, dst):
    if category == "temperature":
        return convert_temperature(value, src.upper(), dst.upper())
    table = UNITS[category]
    return value * table[src] / table[dst]

def main():
    print("📏 UNIT CONVERTER. Categories:", ", ".join([*UNITS, "temperature"]))
    while True:
        cat = ask("\nCategory (or q): ").strip().lower()
        if cat == "q":
            break
        if cat not in UNITS and cat != "temperature":
            print("Unknown category"); continue
        units = "C, F, K" if cat == "temperature" else ", ".join(UNITS[cat])
        print("Units:", units)
        try:
            value = float(ask("Value: "))
            src, dst = ask("From: ").strip(), ask("To: ").strip()
            print(f"✅ {value:g} {src} = {convert(cat, value, src, dst):,.4f} {dst}")
        except (ValueError, KeyError):
            print("❌ Invalid value or unit")

if __name__ == "__main__":
    main()
```

## Extend this project

1. Add currency conversion using fixed rates (or a free API).
2. Show a table converting one value into every unit in its category.
3. Add an electrical category (W, kW, HP, MW).

---

[⬅ Day 131](../Day-131-Project-Menu-Driven-Scientific-Calculator/README.md) · [🏠 Home](../README.md) · [Day 133 ➡](../Day-133-Project-Password-Generator-and-Strength-Checker/README.md)
