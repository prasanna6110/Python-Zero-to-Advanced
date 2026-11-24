# 048 · Closures — Example 3: The late-binding gotcha
# Run: python example_3.py

funcs = [lambda: i for i in range(3)]
print("Buggy:", [f() for f in funcs])        # [2, 2, 2]

funcs = [lambda i=i: i for i in range(3)]
print("Fixed:", [f() for f in funcs])        # [0, 1, 2]
