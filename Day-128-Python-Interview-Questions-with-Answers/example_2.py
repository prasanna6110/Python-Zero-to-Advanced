# Day 128 · Python Interview Questions (with Answers) — Proving the function and OOP answers
# Run: python example_2.py

def outer():
    msg = "I am remembered"
    return lambda: msg
print("closure:", outer()())

def gen():
    yield 1
    yield 2
g = gen()
print("generator:", next(g), next(g))

class A:
    def hi(self): return "A"
class B(A):
    def hi(self): return "B" + super().hi()
class C(A):
    def hi(self): return "C" + super().hi()
class D(B, C): pass
print("MRO:", [k.__name__ for k in D.__mro__], "| D().hi():", D().hi())

class P:
    def __str__(self): return "friendly"
    def __repr__(self): return "P()"
print("str:", str(P()), "| repr:", repr(P()), "| in a list:", [P()])

class Demo:
    count = 0
    @classmethod
    def inc(cls): cls.count += 1; return cls.count
    @staticmethod
    def add(a, b): return a + b
print("classmethod:", Demo.inc(), "| staticmethod:", Demo.add(2, 3))
