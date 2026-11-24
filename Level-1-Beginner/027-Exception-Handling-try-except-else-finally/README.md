# 027 · Exception Handling: try, except, else, finally

## Errors vs exceptions
- **Syntax errors** stop the code before it runs.
- **Exceptions** happen while the code is running: `ZeroDivisionError`, `ValueError`, `TypeError`, `KeyError`, `IndexError`, `FileNotFoundError`...

## Structure
```python
try:
    risky()
except ValueError as e:      # handle one specific error
    ...
except (KeyError, IndexError):
    ...
else:                        # runs if NO exception happened
    ...
finally:                     # ALWAYS runs (cleanup)
    ...
```
## Best practices
- Catch **specific** exceptions. Avoid a bare `except:`.
- Keep the `try` block small.
- Never silently swallow errors without at least logging them.

## Examples

### Example 1: Handling bad input  ([`example_1.py`](example_1.py))

```python
for raw in ["42", "abc", "0"]:
    try:
        n = int(raw)
        result = 100 / n
    except ValueError:
        print(f"{raw!r}: not a number")
    except ZeroDivisionError:
        print(f"{raw!r}: cannot divide by zero")
    else:
        print(f"{raw!r}: 100/{n} = {result}")
    finally:
        print("  checked", raw)
```

### Example 2: Catching and inspecting the exception  ([`example_2.py`](example_2.py))

```python
data = {"a": 1}
items = [1, 2, 3]
tests = [lambda: data["z"], lambda: items[10], lambda: "x" + 5]
for test in tests:
    try:
        test()
    except (KeyError, IndexError) as e:
        print("Lookup problem:", type(e).__name__, e)
    except Exception as e:
        print("Other problem:", type(e).__name__, "-", e)
```

### Example 3: Retrying with a safe input function  ([`example_3.py`](example_3.py))

```python
def safe_int(values):
    """Try each value until one is a valid int (simulates repeated input)."""
    for attempt, v in enumerate(values, 1):
        try:
            return int(v)
        except ValueError:
            print(f"Attempt {attempt}: {v!r} is invalid, try again")
    return None

print("Got:", safe_int(["ten", "1O", "10"]))
```

## Practice

1. Write a calculator that handles division by zero and invalid input.
2. Read a list index from the user and handle IndexError.
3. Show that `finally` runs even when there's a `return` inside `try`.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
