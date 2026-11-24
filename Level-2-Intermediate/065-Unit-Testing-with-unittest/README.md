# 065 · Unit Testing with unittest

## Why test?
Tests prove your code works and protect it from breaking when you change things later.

## unittest (built in)
```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self): ...          # runs before each test
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```
## Common asserts
`assertEqual, assertNotEqual, assertTrue, assertFalse, assertIn, assertIsNone, assertRaises, assertAlmostEqual, assertIsInstance`

Run every test in a project: `python -m unittest discover`.

**AAA pattern**: Arrange → Act → Assert.

## Examples

### Example 1: Testing simple functions  ([`example_1.py`](example_1.py))

```python
import unittest

def is_palindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_palindrome("madam"))

    def test_sentence(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

### Example 2: setUp and assertRaises  ([`example_2.py`](example_2.py))

```python
import unittest

class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = Account(100)

    def test_withdraw(self):
        self.acc.withdraw(30)
        self.assertEqual(self.acc.balance, 70)

    def test_overdraw(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(500)

    def test_balance_unchanged_after_error(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(500)
        self.assertEqual(self.acc.balance, 100)

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

### Example 3: subTest for many inputs  ([`example_3.py`](example_3.py))

```python
import unittest

def grade(marks):
    if marks >= 90: return "A"
    if marks >= 75: return "B"
    if marks >= 40: return "C"
    return "F"

class TestGrade(unittest.TestCase):
    def test_many(self):
        cases = [(95, "A"), (90, "A"), (80, "B"), (40, "C"), (10, "F")]
        for marks, expected in cases:
            with self.subTest(marks=marks):
                self.assertEqual(grade(marks), expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## Practice

1. Write tests for a `Stack` class (push, pop, an empty pop raising an error).
2. Write tests for a string-reversing function, including edge cases (empty string, one character).
3. Deliberately break a function and watch the tests fail.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
