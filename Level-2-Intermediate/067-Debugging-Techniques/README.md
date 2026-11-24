# 067 · Debugging Techniques

## Reading tracebacks
Read them **from the bottom up**. The last line gives the error type and message, and the lines above show the chain of calls that led there.

## Tools
| Tool | Use |
|------|-----|
| `print()` / f"{x=}" | quick checks |
| `breakpoint()` | pauses the program in **pdb**, the interactive debugger |
| `logging` | permanent diagnostics |
| `assert` | sanity checks |
| `traceback` module | format or print tracebacks yourself |
| IDE debugger (VS Code) | breakpoints, watches, stepping |

## pdb commands
`n` (next line), `s` (step into), `c` (continue), `p x` (print x), `l` (list code), `w` (where), `q` (quit)

## Strategy
Reproduce the bug → isolate it → form a hypothesis → test it → fix it → **add a test** so it can't come back.

## Examples

### Example 1: Reading and formatting tracebacks  ([`example_1.py`](example_1.py))

```python
import traceback

def level3(data):
    return data["missing"]

def level2(data):
    return level3(data)

def level1():
    return level2({"a": 1})

try:
    level1()
except KeyError:
    print("Traceback (read from the bottom up):")
    print(traceback.format_exc())
```

### Example 2: Debug prints and assertions  ([`example_2.py`](example_2.py))

```python
def average(nums):
    assert len(nums) > 0, "nums must not be empty"
    total = sum(nums)
    print(f"DEBUG {total=} {len(nums)=}")
    return total / len(nums)

print(average([3, 4, 5]))
try:
    average([])
except AssertionError as e:
    print("AssertionError:", e)
```

### Example 3: Driving pdb from a script  ([`example_3.py`](example_3.py))

```python
import pdb, io, sys

def buggy_sum(n):
    total = 0
    for i in range(n):     # bug: should be range(n + 1)
        total += i
    return total

# Normally you would put breakpoint() inside buggy_sum and type commands yourself.
# Here we feed pdb commands automatically to show what a session looks like.
commands = io.StringIO("p n\nn\nn\np total\nc\n")
debugger = pdb.Pdb(stdin=commands, stdout=sys.stdout)
debugger.use_rawinput = False
result = debugger.runcall(buggy_sum, 5)
print("\nResult:", result, "(expected 15 -> found the bug!)")
```

## Practice

1. Put `breakpoint()` in a loop and inspect the variables while it runs.
2. Deliberately cause 5 different exceptions and read each traceback.
3. Debug a function that returns the wrong maximum of a list.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
