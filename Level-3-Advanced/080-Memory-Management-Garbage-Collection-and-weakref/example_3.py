# 080 · Memory Management, Garbage Collection and weakref — Example 3: weakref caches and finalizers
# Run: python example_3.py

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
