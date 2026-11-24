# 014 · break, continue, pass and loop-else

## Loop control
| Keyword | Effect |
|---------|--------|
| `break` | leave the loop immediately |
| `continue` | skip the rest of this iteration and go to the next one |
| `pass` | do nothing (a placeholder where Python needs a statement) |

## Loop `else`
A `for` or `while` loop can have an `else` block. It runs **only if the loop ended normally**, meaning without hitting `break`. It's perfect for searches: "found it" goes in the loop, "not found" goes in the `else`.

## Examples

### Example 1: break and continue  ([`example_1.py`](example_1.py))

```python
for n in range(1, 11):
    if n == 8:
        break          # stop completely at 8
    if n % 2 == 0:
        continue       # skip even numbers
    print(n)
```

### Example 2: pass as a placeholder  ([`example_2.py`](example_2.py))

```python
def feature_coming_soon():
    pass               # will be written later

class EmptyModel:
    pass

for i in range(3):
    if i == 1:
        pass           # TODO: handle this case
    else:
        print("Processing", i)
print("pass lets code run before it's finished")
```

### Example 3: Loop-else for searching (prime check)  ([`example_3.py`](example_3.py))

```python
for n in [7, 12, 29]:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            print(f"{n} is not prime (divisible by {d})")
            break
    else:
        print(f"{n} is prime")
```

## Practice

1. Print all primes between 1 and 50 using loop-else.
2. Print the numbers from 1 to 20, skipping multiples of 3, using `continue`.
3. Search a list for a name and print "Not found" using loop-else.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
