# 086 · Functional Programming in Python

## Functional programming ideas
- **Pure functions**: the same input always gives the same output, with no side effects.
- **Immutability**: create new data instead of changing old data.
- **First-class and higher-order functions**: functions can take and return functions.
- **Composition**: build big functions out of small ones.
- **Declarative style**: say *what* you want, not *how* to get it.

## Python's FP tools
`map, filter, functools.reduce, partial, lambda, comprehensions, generators, itertools, operator, tuple/frozenset, NamedTuple, dataclass(frozen=True)`

## Techniques
- **Currying**: `f(a)(b)(c)` instead of `f(a, b, c)`.
- **Function composition**: `compose(f, g)(x) == f(g(x))`.
- Python doesn't optimise tail recursion, so prefer iteration or `reduce`.

## Examples

### Example 1: Pure vs impure and immutability  ([`example_1.py`](example_1.py))

```python
total = 0
def impure_add(x):            # changes outside state
    global total
    total += x
    return total

def pure_add(a, b):           # depends only on its inputs
    return a + b

print(impure_add(5), impure_add(5), "<- same input, different output")
print(pure_add(5, 5), pure_add(5, 5))

prices = (100, 200, 300)                       # immutable tuple
discounted = tuple(p * 0.9 for p in prices)    # a new tuple, the original is safe
print(prices, discounted)
```

### Example 2: Composition and pipelines  ([`example_2.py`](example_2.py))

```python
from functools import reduce

def compose(*funcs):
    return lambda x: reduce(lambda acc, f: f(acc), reversed(funcs), x)

def pipe(*funcs):
    return lambda x: reduce(lambda acc, f: f(acc), funcs, x)

strip = str.strip
lower = str.lower
words = str.split
unique_sorted = lambda ws: sorted(set(ws))

clean = pipe(strip, lower, words, unique_sorted)
print(clean("   The quick brown fox jumps over THE lazy dog   "))
inc = lambda x: x + 1
dbl = lambda x: x * 2
print(compose(inc, dbl)(5), pipe(inc, dbl)(5))   # inc(dbl(5)) vs dbl(inc(5))
```

### Example 3: Currying and the operator module  ([`example_3.py`](example_3.py))

```python
from functools import partial, reduce
import operator

def curry(f, n):
    def curried(*args):
        if len(args) >= n:
            return f(*args)
        return lambda *more: curried(*args, *more)
    return curried

volume = curry(lambda l, w, h: l * w * h, 3)
print(volume(2)(3)(4), volume(2, 3)(4), volume(2, 3, 4))

orders = [{"item": "pen", "qty": 3, "price": 10}, {"item": "book", "qty": 2, "price": 250}]
get_cost = lambda o: operator.mul(o["qty"], o["price"])
print(reduce(operator.add, map(get_cost, orders)))
print(list(map(partial(operator.mul, 3), [1, 2, 3])))
print(sorted(orders, key=operator.itemgetter("price"), reverse=True)[0]["item"])
```

## Practice

1. Rewrite a loop-heavy program in a functional style.
2. Implement your own `my_map` and `my_filter` using `reduce`.
3. Build a data-cleaning pipeline using `pipe()` with 5 steps.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
