# 005 · Taking User Input

## input()
`input(prompt)` shows the prompt, waits for the user to type and press Enter, then **always returns a string**.

```python
age = int(input("Enter age: "))
```

## Tips
- Convert the input to a number with `int()` or `float()` before doing maths with it.
- Use `.strip()` to remove extra spaces.
- Use `.split()` to read several values from one line.
- Validate input with `try/except` (covered in a later topic) so bad input doesn't crash the program.

> When you run the examples, type a value and press Enter.

## Examples

### Example 1: Simple greeting  ([`example_1.py`](example_1.py))

```python
name = input("What is your name? ")
print("Hello,", name.strip() + "!")
```

### Example 2: Adding two numbers  ([`example_2.py`](example_2.py))

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum =", a + b)
print("Product =", a * b)
```

### Example 3: Several values in one line  ([`example_3.py`](example_3.py))

```python
# Type something like: 10 20 30
data = input("Enter numbers separated by space: ")
numbers = [int(x) for x in data.split()]
print("You entered:", numbers)
print("Total:", sum(numbers))
```

## Practice

1. Ask for the length and breadth of a rectangle and print its area and perimeter.
2. Ask for a temperature in Celsius and print it in Fahrenheit.
3. Read 5 marks on one line and print their average.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
