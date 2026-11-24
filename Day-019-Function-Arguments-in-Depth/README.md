# Day 019 · Function Arguments in Depth

_Beginner_

## Kinds of arguments
| Kind | Example |
|------|---------|
| Positional | `f(1, 2)` |
| Keyword | `f(a=1, b=2)` |
| Default | `def f(a, b=10)` |
| Variable positional | `def f(*args)` collects extras into a **tuple** |
| Variable keyword | `def f(**kwargs)` collects extras into a **dict** |
| Positional-only | `def f(a, b, /)` |
| Keyword-only | `def f(*, a, b)` |

Order in a definition: `def f(pos_only, /, normal, *args, kw_only, **kwargs)`

## ⚠️ The mutable default trap
`def f(x, items=[])` creates the list **once**, so every call shares it. Use `items=None` and create the list inside the function.

## Unpacking when calling
`f(*my_list)` and `f(**my_dict)`.

## Examples

### Example 1: Default and keyword arguments  ([`example_1.py`](example_1.py))

```python
def make_coffee(size="medium", sugar=1, milk=True):
    return f"{size} coffee, {sugar} sugar, {'with' if milk else 'no'} milk"

print(make_coffee())
print(make_coffee("large"))
print(make_coffee(sugar=0, milk=False))
```

### Example 2: *args and **kwargs  ([`example_2.py`](example_2.py))

```python
def total(*numbers):
    print("args tuple:", numbers)
    return sum(numbers)

def profile(name, **details):
    print("Name:", name)
    for key, value in details.items():
        print(f"  {key}: {value}")

print(total(1, 2, 3, 4))
profile("Kiran", age=22, city="Pune", branch="ECE")

nums = [10, 20, 30]
info = {"age": 30, "city": "Delhi"}
print(total(*nums))
profile("Mohan", **info)
```

### Example 3: Positional-only, keyword-only and the mutable default bug  ([`example_3.py`](example_3.py))

```python
def power(base, exp, /, *, verbose=False):
    result = base ** exp
    if verbose:
        print(f"{base}^{exp} = {result}")
    return result

power(2, 5, verbose=True)
# power(base=2, exp=5) -> TypeError (positional-only)

def bad_append(x, items=[]):
    items.append(x)
    return items

def good_append(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

print(bad_append(1), bad_append(2))    # shared list!
print(good_append(1), good_append(2))
```

## Practice

1. Write `average(*nums)` that works with any number of arguments.
2. Write `build_url(base, **params)` that returns `base?k1=v1&k2=v2`.
3. Explain why `def f(a=[])` is dangerous.

---

[⬅ Day 018](../Day-018-Functions-Basics/README.md) · [🏠 Home](../README.md) · [Day 020 ➡](../Day-020-Scope-LEGB-global-and-nonlocal/README.md)
