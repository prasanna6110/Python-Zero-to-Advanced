# Day 127 · Common Mistakes and Gotchas

_Ultra Advanced_

## Mistakes that confuse almost every student
| # | Mistake | Fix |
|---|---------|-----|
| 1 | A mutable default argument `def f(x=[])` | use `None`, then create the list inside |
| 2 | `a = b = []` shares one list | create them separately |
| 3 | `[[0] * 3] * 3` makes 3 references to the same row | `[[0] * 3 for _ in range(3)]` |
| 4 | Changing a list while looping over it | loop over a copy, or use a comprehension |
| 5 | `is` instead of `==` | use `is` only with `None`, `True` and `False` |
| 6 | Integer vs float division (`/` vs `//`) | know which one you need |
| 7 | Late binding in closures and lambdas | `lambda i=i: i` |
| 8 | A bare `except:` hides bugs | catch specific exceptions |
| 9 | Naming a file `random.py` or `math.py` | it shadows the standard library module! |
| 10 | `input()` returns a string | convert it with `int()` or `float()` |
| 11 | Floating-point comparison | `math.isclose` |
| 12 | Forgetting `self` in methods | `def method(self, ...)` |
| 13 | Reusing an exhausted iterator or generator | create it again |
| 14 | Shadowing built-ins (`list = [...]`, `sum = 0`) | choose other names |
| 15 | `sort()` returns None: `x = lst.sort()` | use `sorted(lst)` |
| 16 | A tuple with one item needs a comma: `(1,)` | |
| 17 | Missing `global` or `nonlocal` gives UnboundLocalError | declare it, or return values instead |
| 18 | Comparing a string number: `"10" > "9"` is False | convert to int first |

## Examples

### Example 1: List and reference gotchas  ([`example_1.py`](example_1.py))

```python
grid = [[0] * 3] * 3
grid[0][0] = 1
print("Bug :", grid)
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 1
print("Fixed:", grid)

nums = [1, 2, 2, 3, 4]
for n in nums:
    if n == 2:
        nums.remove(n)                 # changing the list while looping over it
print("Bug  (should be [1, 3, 4]):", nums)
nums = [1, 2, 2, 3, 4]
print("Fixed:", [n for n in nums if n != 2])

a = b = []
a.append(1)
print("a = b = [] shares one list:", b)
lst = [3, 1, 2]
print("lst.sort() returns:", lst.sort(), "| sorted(lst) returns:", sorted([3, 1, 2]))
```

### Example 2: Scope, iterators and type gotchas  ([`example_2.py`](example_2.py))

```python
count = 0
def increment():
    try:
        count += 1                     # UnboundLocalError
    except UnboundLocalError as e:
        print("UnboundLocalError:", e)
increment()

squares = (x * x for x in range(3))
print(list(squares), list(squares), "<- a generator can only be used once")

print('"10" > "9" ->', "10" > "9", "| 10 > 9 ->", 10 > 9)
print("3 / 2 =", 3 / 2, "| 3 // 2 =", 3 // 2, "| -3 // 2 =", -3 // 2)
print("(1) is", type((1)).__name__, "| (1,) is", type((1,)).__name__)
print("0.1 * 3 == 0.3 ->", 0.1 * 3 == 0.3)
print("True + True =", True + True, "(bool is a subclass of int)")
```

### Example 3: Shadowing, mutable defaults and string immutability  ([`example_3.py`](example_3.py))

```python
list_backup = list
list = [1, 2, 3]                      # shadows the built-in list()
try:
    list("abc")
except TypeError as e:
    print("Shadowing bug:", e)
list = list_backup

def add_student(name, group=[]):
    group.append(name)
    return group
print(add_student("A"), add_student("B"), "<- the same list is reused!")

s = "hello"
s.upper()
print("s.upper() without assigning it:", s, "| s = s.upper():", s.upper())

import random, os
print("If you name your own file random.py, `import random` loads YOUR file.")
print("The real random module lives at:", os.path.basename(os.path.dirname(random.__file__)) + "/random.py")
```

## Practice

1. Find the bug: `def avg(nums=[]): nums.append(0); return sum(nums)/len(nums)`.
2. Explain why `"abc" * 0 == ""` and `[] * 5 == []`.
3. Write down 3 mistakes you made during this course, and how you fixed them.

---

[⬅ Day 126](../Day-126-Writing-Pythonic-Code-Idioms-and-Best-Practices/README.md) · [🏠 Home](../README.md) · [Day 128 ➡](../Day-128-Python-Interview-Questions-with-Answers/README.md)
