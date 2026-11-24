# Day 033 · Exception Handling: try, except, else, finally — Handling bad input
# Run: python example_1.py

for raw in ["42", "abc", "0"]:
    try:
        n = int(raw)
        result = 100 / n
    except ValueError:
        print(f"{raw!r}: not a number")
    except ZeroDivisionError:
        print(f"{raw!r}: cannot divide by zero")
    else:
        print(f"{raw!r}: 100/{n} = {result}")
    finally:
        print("  checked", raw)
