# Day 033 · Exception Handling: try, except, else, finally — Catching and inspecting the exception
# Run: python example_2.py

data = {"a": 1}
items = [1, 2, 3]
tests = [lambda: data["z"], lambda: items[10], lambda: "x" + 5]
for test in tests:
    try:
        test()
    except (KeyError, IndexError) as e:
        print("Lookup problem:", type(e).__name__, e)
    except Exception as e:
        print("Other problem:", type(e).__name__, "-", e)
