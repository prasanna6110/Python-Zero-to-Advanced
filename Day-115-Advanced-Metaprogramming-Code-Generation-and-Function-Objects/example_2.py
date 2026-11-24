# Day 115 · Advanced Metaprogramming: Code Generation and Function Objects — Building and modifying functions with code objects
# Run: python example_2.py

import types

def template(x):
    return x + 1

code = template.__code__
new_code = code.replace(co_consts=tuple(10 if c == 1 else c for c in code.co_consts))
add_ten = types.FunctionType(new_code, globals(), "add_ten")
print(template(5), add_ten(5))

def make_adder(n):
    def adder(x): return x + n
    return adder
a5 = make_adder(5)
clone = types.FunctionType(a5.__code__, a5.__globals__, "clone", None, a5.__closure__)
print("cloned closure:", clone(100), "| closure value:", a5.__closure__[0].cell_contents)

ns = types.SimpleNamespace(host="localhost", port=8000)
ns.debug = True
print(ns)
ro = types.MappingProxyType({"a": 1})
try:
    ro["b"] = 2
except TypeError as e:
    print("read-only mapping:", e)
