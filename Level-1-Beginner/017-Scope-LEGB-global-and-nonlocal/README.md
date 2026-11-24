# 017 · Scope: LEGB, global and nonlocal

## LEGB rule: where Python looks up a name
1. **L**ocal: inside the current function
2. **E**nclosing: inside outer functions (for nested functions)
3. **G**lobal: at the module level
4. **B**uilt-in: names like `len`, `print`

## Changing variables from outer scopes
- `global x` lets a function change a module-level `x`.
- `nonlocal x` lets a nested function change `x` from the enclosing function.

Use global state sparingly. Passing arguments and returning values is cleaner.

## Examples

### Example 1: LEGB in action  ([`example_1.py`](example_1.py))

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("inner sees:", x)
    inner()
    print("outer sees:", x)

outer()
print("module sees:", x)
print("built-in len:", len("abc"))
```

### Example 2: global keyword  ([`example_2.py`](example_2.py))

```python
counter = 0

def increment():
    global counter
    counter += 1

for _ in range(5):
    increment()
print("counter =", counter)
```

### Example 3: nonlocal keyword  ([`example_3.py`](example_3.py))

```python
def make_counter():
    count = 0
    def step():
        nonlocal count
        count += 1
        return count
    return step

c = make_counter()
print(c(), c(), c())
c2 = make_counter()
print(c2())    # each counter keeps its own state
```

## Practice

1. Predict the output before you run Example 1.
2. What error do you get if you remove `global` in Example 2? Why?
3. Write `make_accumulator()` that returns a function adding to a running total.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
