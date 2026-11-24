# 066 · pytest and doctest

## pytest (`pip install pytest`): the most popular testing tool
- Tests are plain functions named `test_*` that use a plain `assert`.
- **Fixtures** provide reusable setup through `@pytest.fixture`.
- **Parametrize** runs one test with many inputs.
- Run it with `pytest -v` (it finds `test_*.py` files automatically).

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected
```
## doctest
Tests written **inside docstrings** that look like a REPL session. They double as documentation.
```python
def square(x):
    """
    >>> square(3)
    9
    """
```
Run them with `python -m doctest file.py -v`.

## Examples

### Example 1: doctest  ([`example_1.py`](example_1.py))

```python
def factorial(n):
    """Return n!.

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: n must be >= 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    return 1 if n == 0 else n * factorial(n - 1)

if __name__ == "__main__":
    import doctest
    results = doctest.testmod(verbose=False)
    print(results)
```

### Example 2: pytest-style tests (works with or without pytest installed)  ([`example_2.py`](example_2.py))

```python
# Save as test_cart.py and run:  pytest -v
try:
    import pytest
except ImportError:
    pytest = None

def cart_total(prices, discount=0):
    if not 0 <= discount <= 100:
        raise ValueError("bad discount")
    return round(sum(prices) * (1 - discount / 100), 2)

def test_total():
    assert cart_total([100, 200]) == 300

def test_discount():
    assert cart_total([100], discount=10) == 90

def test_bad_discount():
    try:
        cart_total([1], discount=200)
        assert False, "expected ValueError"
    except ValueError:
        pass

if __name__ == "__main__":
    for t in [test_total, test_discount, test_bad_discount]:
        t()
        print("PASSED", t.__name__)
    print("pytest installed:", pytest is not None)
```

### Example 3: Fixtures and parametrize (pytest file content)  ([`example_3.py`](example_3.py))

```python
# This shows a real pytest file. Running this example writes it out
# and runs it with pytest if pytest is installed.
import pathlib, subprocess, sys, importlib.util

TEST_CODE = '''
import pytest

@pytest.fixture
def inventory():
    return {"apple": 5, "mango": 0}

def test_in_stock(inventory):
    assert inventory["apple"] > 0

@pytest.mark.parametrize("word,expected", [("level", True), ("hello", False), ("", True)])
def test_palindrome(word, expected):
    assert (word == word[::-1]) is expected
'''
path = pathlib.Path("test_demo_pytest.py")
path.write_text(TEST_CODE)
if importlib.util.find_spec("pytest"):
    subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(path)])
else:
    print("pytest not installed. Run: pip install pytest")
    print(TEST_CODE)
path.unlink()
```

## Practice

1. Convert your unittest tests from the previous topic to pytest.
2. Write doctests for 3 utility functions.
3. Write a fixture that creates a temporary file (hint: the built-in `tmp_path` fixture).

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
