# 015 · Functions Basics

## What is a function?
A **reusable, named block of code** that does one job. It follows **DRY** (Don't Repeat Yourself).

```python
def function_name(parameters):
    """Docstring: what the function does."""
    # body
    return value
```
- **Parameter**: the variable in the definition. **Argument**: the value you pass when calling.
- A function with no `return` gives back `None`.
- `return` can give back several values as a tuple: `return a, b`.
- In Python, functions are **objects**. You can store them in variables and pass them around.

## Examples

### Example 1: Defining and calling  ([`example_1.py`](example_1.py))

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Ananya"))
print(greet("Rahul"))
print(greet.__doc__)
```

### Example 2: Returning multiple values  ([`example_2.py`](example_2.py))

```python
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = stats([4, 8, 15, 16, 23, 42])
print(f"min={low} max={high} avg={avg:.2f}")

def say_hi():
    print("hi")
result = say_hi()
print("Return value of say_hi:", result)   # None
```

### Example 3: Functions are objects  ([`example_3.py`](example_3.py))

```python
def square(x):
    return x * x

def cube(x):
    return x ** 3

operations = {"square": square, "cube": cube}
for name, func in operations.items():
    print(name, func(3))

f = square            # assign a function to a variable
print(f(9), f.__name__)
```

## Practice

1. Write `is_even(n)` that returns True or False.
2. Write `celsius_to_fahrenheit(c)`.
3. Write `count_vowels(text)` and test it on 3 sentences.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
