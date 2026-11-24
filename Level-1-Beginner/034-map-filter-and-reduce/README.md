# 034 · map, filter and reduce

## map(func, iterable)
Applies `func` to every item. It returns a **lazy iterator**, so wrap it in `list()` to see the results.

## filter(func, iterable)
Keeps only the items for which `func(item)` is truthy.

## functools.reduce(func, iterable, initial)
Combines all the items into **one value**: `reduce(f, [a, b, c])` works out `f(f(a, b), c)`.

## Comprehensions vs map/filter
`[x*2 for x in nums]` is often more readable than `list(map(lambda x: x*2, nums))`. Both are fine. Pick whichever reads more clearly.

## Examples

### Example 1: map  ([`example_1.py`](example_1.py))

```python
nums = [1, 2, 3, 4]
print(list(map(lambda x: x * x, nums)))
print(list(map(str.upper, ["a", "b"])))
print(list(map(int, "1 2 3".split())))
print(list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])))
```

### Example 2: filter  ([`example_2.py`](example_2.py))

```python
nums = range(1, 21)
print(list(filter(lambda n: n % 3 == 0, nums)))
words = ["", "python", None, "code", 0]
print(list(filter(None, words)))          # removes falsy values
emails = ["a@x.com", "bad", "c@y.org"]
print(list(filter(lambda e: "@" in e, emails)))
```

### Example 3: reduce and a data pipeline  ([`example_3.py`](example_3.py))

```python
from functools import reduce
import operator

print(reduce(operator.add, [1, 2, 3, 4]))
print(reduce(lambda a, b: a * b, range(1, 6)))       # 5!
print(reduce(lambda a, b: a if a > b else b, [3, 9, 2]))

orders = [("pen", 10, 3), ("book", 250, 1), ("bag", 900, 0)]
total = reduce(lambda acc, o: acc + o[1] * o[2],
               filter(lambda o: o[2] > 0, orders), 0)
print("Order total:", total)
```

## Practice

1. Use `map` to convert a list of Celsius temperatures to Fahrenheit.
2. Use `filter` to keep the palindromes from a list of words.
3. Use `reduce` to find the GCD of a list of numbers.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
