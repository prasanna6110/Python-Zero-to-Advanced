# 030 · Modules, Imports and __name__

## Modules
Any `.py` file is a **module**. You reuse code by importing it.

```python
import math
import math as m
from math import sqrt, pi
from math import *        # avoid: it pollutes your namespace
```
## Where Python looks for modules
`sys.path`: the script's folder, then `PYTHONPATH`, then the standard library, then site-packages.

## `if __name__ == "__main__":`
- When you **run** a file directly, `__name__` is `"__main__"`.
- When the file is **imported**, `__name__` is the module's name.
- So code inside this block runs only when the file is executed directly, not when it's imported.

## Useful built-ins
`dir(module)` lists what's inside a module and `help(module)` shows its documentation.

## Examples

### Example 1: Different import styles  ([`example_1.py`](example_1.py))

```python
import math
import random as rnd
from datetime import date
from statistics import mean, median

print(math.pi, math.factorial(5))
rnd.seed(1)
print(rnd.randint(1, 100))
print(date(2026, 1, 13).strftime("%A"))
print(mean([1, 2, 3, 4]), median([5, 1, 9]))
```

### Example 2: Creating and importing your own module  ([`example_2.py`](example_2.py))

```python
import pathlib
import sys

# Create a module file on the fly (normally you write it by hand)
pathlib.Path("mytools.py").write_text(
    'PI = 3.14159\n'
    'def circle_area(r):\n'
    '    return PI * r * r\n'
    'if __name__ == "__main__":\n'
    '    print("mytools run directly")\n'
)
sys.path.insert(0, ".")
import mytools
print(mytools.circle_area(2))
print("module name:", mytools.__name__)
pathlib.Path("mytools.py").unlink()
```

### Example 3: The __name__ guard  ([`example_3.py`](example_3.py))

```python
def main():
    print("Running main program")

print("__name__ is:", __name__)
if __name__ == "__main__":
    main()
```

## Practice

1. Create `calculator.py` with 4 functions and import it from another file.
2. Print `sys.path` and explain each entry.
3. Use `dir(math)` and try 5 functions you haven't used before.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
