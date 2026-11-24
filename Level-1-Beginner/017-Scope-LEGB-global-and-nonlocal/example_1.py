# 017 · Scope: LEGB, global and nonlocal — Example 1: LEGB in action
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
