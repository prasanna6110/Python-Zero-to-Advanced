# Day 015 · while Loops

_Beginner_

## while loop
It repeats **as long as the condition is True**.
```python
while condition:
    ...
```
- Use it when you **don't know in advance** how many times to repeat, for example reading input until the user types "quit".
- Make sure the condition eventually becomes False, otherwise you get an **infinite loop** (press Ctrl+C to stop one).
- `while True:` together with `break` is a common pattern.

## Examples

### Example 1: Counting down  ([`example_1.py`](example_1.py))

```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("Lift off!")
```

### Example 2: Digit operations  ([`example_2.py`](example_2.py))

```python
n = 98765
total, reverse = 0, 0
temp = n
while temp > 0:
    digit = temp % 10
    total += digit
    reverse = reverse * 10 + digit
    temp //= 10
print("Sum of digits:", total)
print("Reversed:", reverse)
```

### Example 3: Guessing game (simulated guesses)  ([`example_3.py`](example_3.py))

```python
secret = 42
guesses = iter([10, 60, 40, 42])   # stands in for input() so the example runs on its own
attempts = 0
while True:
    guess = next(guesses)
    attempts += 1
    if guess < secret:
        print(guess, "-> too low")
    elif guess > secret:
        print(guess, "-> too high")
    else:
        print(guess, f"-> correct in {attempts} attempts!")
        break
```

## Practice

1. Keep asking for numbers until the user enters 0, then print their sum.
2. Print the Fibonacci numbers that are less than 1000.
3. Check whether a number is an Armstrong number (for example 153).

---

[⬅ Day 014](../Day-014-for-Loops-and-range/README.md) · [🏠 Home](../README.md) · [Day 016 ➡](../Day-016-break-continue-pass-and-loop-else/README.md)
