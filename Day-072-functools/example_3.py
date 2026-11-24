# Day 072 · functools — singledispatch: overloading by type
# Run: python example_3.py

from functools import singledispatch

@singledispatch
def describe(obj):
    return f"Something: {obj!r}"

@describe.register
def _(obj: int):
    return f"Integer with {len(str(abs(obj)))} digits"

@describe.register
def _(obj: list):
    return f"List of {len(obj)} items"

@describe.register(str)
def _(obj):
    return f"String of length {len(obj)}"

for item in [42, "hello", [1, 2, 3], 3.14]:
    print(describe(item))
