# Day 079 · __new__ vs __init__ and __slots__ — __new__ runs before __init__
# Run: python example_1.py

class Demo:
    def __new__(cls, *args):
        print(f"__new__ called with {args}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("__init__ called")
        self.value = value

d = Demo(42)
print(d.value)
