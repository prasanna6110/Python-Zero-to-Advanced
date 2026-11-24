# 048 · Closures

## Closure
A **nested function that remembers variables from its enclosing scope**, even after the outer function has finished.

You get a closure when all three of these are true:
1. There is a nested function.
2. It uses a variable from the outer function.
3. The outer function returns the inner function.

The remembered variables are stored in `func.__closure__`.

## Uses
Factory functions, keeping state without a class, callbacks, and **decorators** (next topic).

## ⚠️ The late-binding gotcha
Closures created in a loop all see the **final** value of the loop variable. Fix it with a default argument: `lambda i=i: i`.

## Examples

### Example 1: A basic closure  ([`example_1.py`](example_1.py))

```python
def outer(message):
    def inner():
        print("Message:", message)
    return inner

say_hi = outer("Hi!")
say_bye = outer("Bye!")
say_hi()
say_bye()
print(say_hi.__closure__[0].cell_contents)
```

### Example 2: Closures that keep state  ([`example_2.py`](example_2.py))

```python
def make_averager():
    numbers = []
    def add(n):
        numbers.append(n)
        return sum(numbers) / len(numbers)
    return add

avg = make_averager()
print(avg(10), avg(20), avg(60))

def power_factory(exp):
    return lambda base: base ** exp
square, cube = power_factory(2), power_factory(3)
print(square(5), cube(5))
```

### Example 3: The late-binding gotcha  ([`example_3.py`](example_3.py))

```python
funcs = [lambda: i for i in range(3)]
print("Buggy:", [f() for f in funcs])        # [2, 2, 2]

funcs = [lambda i=i: i for i in range(3)]
print("Fixed:", [f() for f in funcs])        # [0, 1, 2]
```

## Practice

1. Write `make_multiplier(n)` that returns a function multiplying its input by n.
2. Write a closure-based counter with `increment` and `reset` (return both functions).
3. Explain why the "buggy" output in Example 3 happens.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
