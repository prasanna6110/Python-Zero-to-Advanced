# 108 · Tracing, Profiling Hooks and Audit Hooks — Example 1: Building a mini tracer and line coverage tool
# Run: python example_1.py

import sys

def fizz(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)

executed = set()
def tracer(frame, event, arg):
    if frame.f_code.co_name == "fizz":
        if event == "call":
            print(f"call  fizz(n={frame.f_locals['n']})")
        elif event == "line":
            executed.add(frame.f_lineno)
        elif event == "return":
            print(f"return {arg!r}")
    return tracer

sys.settrace(tracer)
fizz(3); fizz(4)
sys.settrace(None)
first = fizz.__code__.co_firstlineno
print("lines executed (relative to the def):", sorted(l - first for l in executed))
