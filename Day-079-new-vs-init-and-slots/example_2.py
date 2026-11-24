# Day 079 · __new__ vs __init__ and __slots__ — Subclassing immutables and caching instances
# Run: python example_2.py

class Celsius(float):
    def __new__(cls, value):
        if value < -273.15:
            raise ValueError("below absolute zero")
        return super().__new__(cls, value)

    def to_f(self):
        return self * 9 / 5 + 32

t = Celsius(36.6)
print(t, t.to_f(), isinstance(t, float))

class Color:
    _cache = {}
    def __new__(cls, name):
        if name not in cls._cache:
            print(f"  creating {name}")
            cls._cache[name] = super().__new__(cls)
        return cls._cache[name]
    def __init__(self, name):
        self.name = name

print(Color("red") is Color("red"), Color("blue") is Color("red"))
