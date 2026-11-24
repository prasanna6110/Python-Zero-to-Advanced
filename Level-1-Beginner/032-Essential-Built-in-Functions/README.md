# 032 · Essential Built-in Functions

## The built-ins you'll use every day
| Function | Use |
|----------|-----|
| `len, type, id, isinstance` | inspecting values |
| `abs, round, pow, divmod, sum, min, max` | maths |
| `sorted, reversed` | ordering |
| `enumerate, zip` | looping |
| `any, all` | boolean checks over iterables |
| `map, filter` | transforming and filtering |
| `range, iter, next` | iteration |
| `input, print, open` | input and output |
| `chr, ord` | characters ↔ code points |
| `eval, exec` | ⚠️ run code from strings (dangerous with untrusted input) |
| `help, dir, vars` | introspection |

`min`, `max` and `sorted` all accept a `key=` function.

## Examples

### Example 1: Maths built-ins  ([`example_1.py`](example_1.py))

```python
print(abs(-7), round(3.14159, 2), pow(2, 10), pow(2, 10, 1000))
print(divmod(17, 5))                # (quotient, remainder)
nums = [4, -9, 2, 7]
print(sum(nums), min(nums), max(nums), max(nums, key=abs))
print(round(2.5), round(3.5))        # banker's rounding: ties go to the nearest even number
```

### Example 2: any, all, zip, enumerate  ([`example_2.py`](example_2.py))

```python
marks = [45, 67, 89, 33]
print("Anyone failed?", any(m < 40 for m in marks))
print("All passed?", all(m >= 40 for m in marks))
names = ["A", "B", "C", "D"]
for i, (n, m) in enumerate(zip(names, marks), 1):
    print(i, n, m)
print(dict(zip(names, marks)))
```

### Example 3: chr, ord, isinstance, iter/next  ([`example_3.py`](example_3.py))

```python
print(ord("A"), chr(97), [chr(c) for c in range(65, 70)])
caesar = "".join(chr((ord(c) - 97 + 3) % 26 + 97) for c in "python")
print("Caesar cipher:", caesar)
for v in [1, 2.0, "3", [4]]:
    print(v, isinstance(v, (int, float)))
it = iter([10, 20])
print(next(it), next(it), next(it, "done"))
```

## Practice

1. Use `max` with `key` to find the longest word in a sentence.
2. Use `all` to check whether a list is sorted.
3. Write ROT13 encoding using `ord` and `chr`.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
