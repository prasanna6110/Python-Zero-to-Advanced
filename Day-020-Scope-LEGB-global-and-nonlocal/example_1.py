# Day 020 · Scope: LEGB, global and nonlocal — LEGB in action
# Run: python example_1.py

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("inner sees:", x)
    inner()
    print("outer sees:", x)

outer()
print("module sees:", x)
print("built-in len:", len("abc"))
