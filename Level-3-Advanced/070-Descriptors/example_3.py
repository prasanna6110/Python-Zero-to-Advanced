# 070 · Descriptors — Example 3: Lazy attributes and how methods bind
# Run: python example_3.py

class Lazy:
    """Non-data descriptor: computes once, then the instance dict takes over."""
    def __init__(self, func):
        self.func = func
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        obj.__dict__[self.name] = value     # later lookups skip the descriptor
        return value

class Report:
    @Lazy
    def data(self):
        print("  loading data...")
        return list(range(5))

r = Report()
print(r.data)
print(r.data)

def greet(self): return f"hi from {self}"
class A: pass
bound = greet.__get__(A(), A)          # exactly what Python does for methods
print(bound, "->", bound()[:10])
