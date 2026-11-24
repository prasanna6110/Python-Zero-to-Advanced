# Day 128 · Python Interview Questions (with Answers)

_Ultra Advanced_

## 40 frequently asked questions (short answers)
**Basics**
1. **Is Python compiled or interpreted?** Both. Source code is compiled to bytecode, which the PVM interprets.
2. **List vs tuple?** A list is mutable. A tuple is immutable, hashable (if its items are) and slightly faster.
3. **`is` vs `==`?** Identity vs equality.
4. **What are `*args` and `**kwargs`?** Variable positional and keyword arguments.
5. **Mutable vs immutable types?** list, dict and set are mutable. int, str, tuple and frozenset are immutable.
6. **What does `pass` do?** Nothing. It's a placeholder.
7. **`append` vs `extend`?** `append` adds one item. `extend` adds every item from an iterable.
8. **`remove` vs `pop` vs `del`?** `remove` deletes by value, `pop` by index (and returns the item), and `del` deletes by index, slice or name.
9. **How does Python manage memory?** Reference counting plus a cyclic garbage collector, using a private heap.
10. **What is PEP 8?** The style guide.

**Functions**
11. **What is a lambda?** An anonymous single-expression function.
12. **What is a decorator?** A function that wraps another function to add behaviour.
13. **What is a closure?** An inner function that remembers variables from its enclosing scope.
14. **What is the LEGB rule?** Local → Enclosing → Global → Built-in.
15. **Generator vs normal function?** `yield` produces values lazily and pauses the function's state.
16. **`map`, `filter`, `reduce`?** Transform, select, combine.
17. **Shallow vs deep copy?** A shallow copy shares the nested objects. A deep copy copies everything recursively.
18. **Why is a mutable default argument dangerous?** It's created once and shared between calls.

**OOP**
19. **What is `self`?** The instance, passed automatically to methods.
20. **`__init__` vs `__new__`?** `__init__` initialises an object. `__new__` creates it.
21. **classmethod vs staticmethod?** A classmethod gets `cls`. A staticmethod gets nothing.
22. **What is the MRO?** The method resolution order (C3 linearisation).
23. **`__str__` vs `__repr__`?** User-friendly vs developer/unambiguous.
24. **What is duck typing?** Behaviour matters more than type.
25. **Does Python have private members?** Only by convention (`_x`) and name mangling (`__x`).
26. **What is a metaclass?** The class of a class (`type`).

**Advanced**
27. **What is the GIL?** A lock that lets only one thread run Python bytecode at a time.
28. **Threads vs processes vs asyncio?** I/O-bound vs CPU-bound vs many concurrent I/O tasks.
29. **What is a context manager?** An object with `__enter__`/`__exit__`, used with `with`.
30. **Iterator vs iterable?** An iterator has `__next__`. An iterable has `__iter__`.
31. **What does `if __name__ == "__main__"` mean?** The code runs only when the file is executed directly.
32. **What are `.pyc` files?** Cached bytecode.
33. **What does `@property` do?** It lets a method be accessed like an attribute (getters and setters).
34. **What is monkey patching?** Changing code while the program runs.
35. **What is pickling?** Serialising objects to bytes.
36. **What are `__slots__`?** They fix the attribute set and save memory.
37. **How do you handle exceptions?** `try`/`except`/`else`/`finally`, plus custom exception classes.
38. **What is a virtual environment?** An isolated set of packages for each project.
39. **What's the time complexity of dict lookup?** O(1) on average.
40. **How do you reverse a list?** `lst[::-1]`, `reversed()` or `lst.reverse()`.

The examples below **prove** the trickiest answers in code.

## Examples

### Example 1: Proving the basics in code  ([`example_1.py`](example_1.py))

```python
import copy

a = [1, [2, 3]]
shallow, deep = copy.copy(a), copy.deepcopy(a)
a[1].append(4)
print("shallow shares nested:", shallow, "| deep is independent:", deep)

x = [1, 2]; y = [1, 2]
print("x == y:", x == y, "| x is y:", x is y)

lst = [1, 2]
lst.append([3, 4]); print("append:", lst)
lst = [1, 2]
lst.extend([3, 4]); print("extend:", lst)
lst.remove(3); print("remove(3):", lst, "| pop():", lst.pop(), "->", lst)

t = (1, 2)
try:
    t[0] = 5
except TypeError as e:
    print("tuple is immutable:", e)
print("hashable tuple as key:", {(1, 2): "ok"})
```

### Example 2: Proving the function and OOP answers  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Proving the advanced answers  ([`example_3.py`](example_3.py))

```python
import sys, threading, time, timeit

class Slot:
    __slots__ = ("a",)
try:
    s = Slot(); s.b = 1
except AttributeError as e:
    print("__slots__:", e)

print("metaclass of int:", type(int), "| of type:", type(type))
print("refcount of a new list:", sys.getrefcount([]))

d = {i: i for i in range(100_000)}
l = list(range(100_000))
print("dict lookup :", round(timeit.timeit(lambda: 99_999 in d, number=1000), 5), "s")
print("list lookup :", round(timeit.timeit(lambda: 99_999 in l, number=1000), 5), "s")

def io(): time.sleep(0.2)
t = time.perf_counter()
ts = [threading.Thread(target=io) for _ in range(5)]
[x.start() for x in ts]; [x.join() for x in ts]
print(f"5 I/O tasks in threads: {time.perf_counter() - t:.2f}s (the GIL is released while waiting)")
print("__name__ here is:", __name__)
```

## Practice

1. Answer every question out loud without looking, then check your answers.
2. Write your own code to prove 5 more of the answers.
3. Do a mock interview with a friend using these questions.

---

[⬅ Day 127](../Day-127-Common-Mistakes-and-Gotchas/README.md) · [🏠 Home](../README.md) · [Day 129 ➡](../Day-129-Project-Number-Guessing-Game/README.md)
