# Day 090 · Memory Management, Garbage Collection and weakref

_Advanced_

## How CPython manages memory
1. **Reference counting**: every object counts how many references point to it. When the count drops to 0, the object is freed **immediately**.
2. **Cyclic garbage collector** (`gc` module): finds and frees **reference cycles** (A → B → A) that counting alone can't free. It sorts objects into 3 generations.
3. **pymalloc**: a fast allocator for small objects.

## Tools
- `sys.getrefcount(obj)` (the result is 1 higher than you'd expect, because of the argument itself)
- `gc.collect()`, `gc.get_count()`, `gc.disable()`
- `sys.getsizeof(obj)` gives the size of the object itself, **not** the things it contains
- `weakref` lets you refer to an object **without keeping it alive**. It's used for caches and observers.

## Interning and small-integer caching
The integers from -5 to 256 and many short strings are **cached**, which is why `a is b` can be True for them. Never rely on that behaviour.

## Examples

### Example 1: Reference counting  ([`example_1.py`](example_1.py))

```python
import sys

data = [1, 2, 3]
print("refcount:", sys.getrefcount(data))
alias = data
container = [data, data]
print("after 3 more refs:", sys.getrefcount(data))
del alias
container.clear()
print("after removing them:", sys.getrefcount(data))

a, b = 256, 256
c, d = int("257"), int("257")
print(a is b, c is d, "<- small int cache (implementation detail)")
```

### Example 2: Reference cycles and the gc  ([`example_2.py`](example_2.py))

```python
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None
    def __del__(self):
        print(f"  freeing {self.name}")

gc.disable()
a, b = Node("A"), Node("B")
a.partner, b.partner = b, a          # cycle!
del a, b
print("deleted names, but the cycle keeps them alive...")
print("collected:", gc.collect(), "objects")
gc.enable()
print("gc thresholds:", gc.get_threshold())
```

### Example 3: weakref caches and finalizers  ([`example_3.py`](example_3.py))

```python
import weakref

class Image:
    def __init__(self, name): self.name = name
    def __repr__(self): return f"Image({self.name})"

cache = weakref.WeakValueDictionary()
img = Image("logo.png")
cache["logo"] = img
print("in cache:", dict(cache))
del img                                 # the only strong reference is gone
print("after del:", dict(cache))

obj = Image("temp")
ref = weakref.ref(obj)
weakref.finalize(obj, print, "  finalizer: temp image cleaned up")
print("ref alive:", ref())
del obj
print("ref now:", ref())
```

## Practice

1. Build a cycle with 3 objects and confirm that `gc.collect()` frees them.
2. Write a `deep_getsizeof()` that adds up the sizes of nested containers.
3. Use a `WeakSet` to track live instances of a class.

---

[⬅ Day 089](../Day-089-The-GIL-and-Choosing-the-Right-Concurrency-Model/README.md) · [🏠 Home](../README.md) · [Day 091 ➡](../Day-091-Python-Internals-Bytecode-and-dis/README.md)
