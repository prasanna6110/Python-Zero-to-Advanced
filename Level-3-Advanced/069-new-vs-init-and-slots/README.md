# 069 · __new__ vs __init__ and __slots__

## Object creation happens in two steps
1. `__new__(cls, ...)` **creates** the object. It's a static method that must return the new instance.
2. `__init__(self, ...)` **initialises** the object that was just created.

You rarely override `__new__`. You need it for:
- subclassing **immutable types** (`int`, `str`, `tuple`), whose value must be fixed when they're created
- singletons, instance caching and object pools

## `__slots__`
```python
class Point:
    __slots__ = ("x", "y")
```
- Removes the per-object `__dict__`, which **saves memory** (often 40–60%) and makes attribute access slightly faster.
- Stops you from adding new attributes by accident.
- Trade-offs: no dynamic attributes, and inheritance needs care (every subclass must declare `__slots__` too).

## Examples

### Example 1: __new__ runs before __init__  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: Subclassing immutables and caching instances  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: __slots__ saves memory  ([`example_3.py`](example_3.py))

```python
import sys, tracemalloc

class Normal:
    def __init__(self, x, y): self.x, self.y = x, y

class Slotted:
    __slots__ = ("x", "y")
    def __init__(self, x, y): self.x, self.y = x, y

for cls in (Normal, Slotted):
    tracemalloc.start()
    objs = [cls(i, i) for i in range(100_000)]
    current, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{cls.__name__:<8} {current / 1024 / 1024:.1f} MB for 100k objects")

s = Slotted(1, 2)
try:
    s.z = 3
except AttributeError as e:
    print("AttributeError:", e)
```

## Practice

1. Write a `PositiveInt(int)` class that rejects negative values in `__new__`.
2. Measure the memory of 1 million slotted vs normal objects.
3. Implement a singleton with `__new__`.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
