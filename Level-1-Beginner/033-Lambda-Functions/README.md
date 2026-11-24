# 033 · Lambda Functions

## Lambda
A small **anonymous function** written as a single expression:
```python
lambda arguments: expression
```
`square = lambda x: x * x`

## When to use one
- As a short `key=` for `sorted`, `min` or `max`.
- With `map`, `filter` and `reduce`.
- For callbacks.

## Limits
- It can contain only one expression: no statements and no assignments (except with `:=`).
- If you're giving it a name, a normal `def` is clearer (PEP 8 says so too).

## Examples

### Example 1: Basic lambdas  ([`example_1.py`](example_1.py))

```python
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0
greet = lambda name="Guest": f"Hi {name}"
print(add(3, 4), is_even(10), greet(), greet("Zara"))
print((lambda x: x ** 3)(4))      # call it immediately
```

### Example 2: Sorting with lambda keys  ([`example_2.py`](example_2.py))

```python
students = [
    {"name": "Asha", "cgpa": 8.9, "age": 21},
    {"name": "Ravi", "cgpa": 9.4, "age": 22},
    {"name": "Meera", "cgpa": 8.9, "age": 20},
]
by_cgpa = sorted(students, key=lambda s: (-s["cgpa"], s["name"]))
for s in by_cgpa:
    print(s["name"], s["cgpa"])
print(min(students, key=lambda s: s["age"])["name"])
```

### Example 3: Lambdas returned from functions  ([`example_3.py`](example_3.py))

```python
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print(double(10), triple(10))

ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
       "*": lambda a, b: a * b, "/": lambda a, b: a / b}
for op in ops:
    print(f"8 {op} 2 = {ops[op](8, 2)}")
```

## Practice

1. Sort a list of tuples `(name, salary)` by salary in descending order.
2. Write a lambda that returns the larger of two numbers.
3. Sort the strings in a list by how many vowels they contain.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
