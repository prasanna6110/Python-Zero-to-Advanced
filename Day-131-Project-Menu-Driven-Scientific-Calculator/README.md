# Day 131 · Project: Menu-Driven Scientific Calculator

_Projects_

**Concepts:** functions, a dictionary of operations, `math`, error handling, a menu loop, history.

It supports the basic operations, powers, roots, logarithms, trigonometry and factorials, and keeps a **history** of what you calculated.

## Code

### Scientific Calculator  ([`main.py`](main.py))

```python
import math
import sys

DEMO = not sys.stdin.isatty()
DEMO_INPUTS = iter(["1", "12", "8", "4", "10", "0", "5", "2", "10", "7", "30", "9", "6", "h", "q"])

def ask(prompt):
    if DEMO:
        value = next(DEMO_INPUTS)
        print(prompt + value)
        return value
    return input(prompt)

def read_number(prompt):
    while True:
        try:
            return float(ask(prompt))
        except ValueError:
            print("  Not a number, try again.")

BINARY = {
    "1": ("Add", lambda a, b: a + b),
    "2": ("Subtract", lambda a, b: a - b),
    "3": ("Multiply", lambda a, b: a * b),
    "4": ("Divide", lambda a, b: a / b),
    "5": ("Power", lambda a, b: a ** b),
}
UNARY = {
    "6": ("Square root", math.sqrt),
    "7": ("sin (degrees)", lambda x: math.sin(math.radians(x))),
    "8": ("log10", math.log10),
    "9": ("Factorial", lambda x: math.factorial(int(x))),
}

def main():
    history = []
    while True:
        print("\n===== CALCULATOR =====")
        for k, (name, _) in {**BINARY, **UNARY}.items():
            print(f" {k}. {name}")
        print(" h. History   q. Quit")
        choice = ask("Choose: ").strip().lower()
        try:
            if choice == "q":
                print("Bye! 👋"); break
            elif choice == "h":
                print("\n".join(history) or "No history yet")
            elif choice in BINARY:
                name, fn = BINARY[choice]
                a, b = read_number("  a = "), read_number("  b = ")
                result = fn(a, b)
                history.append(f"{name}({a:g}, {b:g}) = {result:g}")
                print("  Result:", f"{result:g}")
            elif choice in UNARY:
                name, fn = UNARY[choice]
                x = read_number("  x = ")
                result = fn(x)
                history.append(f"{name}({x:g}) = {result:g}")
                print("  Result:", f"{result:g}")
            else:
                print("Invalid choice")
        except ZeroDivisionError:
            print("  ❌ Cannot divide by zero")
        except ValueError as e:
            print("  ❌ Math error:", e)

if __name__ == "__main__":
    main()
```

## Extend this project

1. Add memory buttons (M+, M-, MR).
2. Let the user type a whole expression like `2 + 3 * 4` (parse it safely with `ast`).
3. Build a GUI version with Tkinter (see the Tkinter day).

---

[⬅ Day 130](../Day-130-Project-Rock-Paper-Scissors/README.md) · [🏠 Home](../README.md) · [Day 132 ➡](../Day-132-Project-Unit-Converter/README.md)
