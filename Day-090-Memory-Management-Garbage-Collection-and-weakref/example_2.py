# Day 090 · Memory Management, Garbage Collection and weakref — Reference cycles and the gc
# Run: python example_2.py

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
