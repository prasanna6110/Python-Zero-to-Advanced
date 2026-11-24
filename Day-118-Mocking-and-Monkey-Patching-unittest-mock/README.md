# Day 118 · Mocking and Monkey Patching (unittest.mock)

_Ultra Advanced_

## Why mock?
Tests should be **fast and repeatable**. Replace the slow or unpredictable parts (network calls, databases, time, randomness) with **fake objects**.

## unittest.mock
| Tool | Use |
|------|-----|
| `Mock()` / `MagicMock()` | an object that accepts any call and records how it was used |
| `return_value`, `side_effect` | control what it returns, or raise an exception |
| `assert_called_once_with(...)`, `call_count`, `call_args_list` | verify the calls |
| `patch("module.name")` | temporarily replace something (as a decorator or a context manager) |
| `patch.object(obj, "attr")` | patch one attribute of an object |
| `spec=` / `autospec=True` | make the mock match the real object's API |

⚠️ **Patch where the name is looked up, not where it's defined.** If `app.py` does `from api import fetch`, patch `app.fetch`.

**Monkey patching** means changing a module or class while the program runs. It's powerful, but use it sparingly outside of tests.

## Examples

### Example 1: Mock objects and side_effect  ([`example_1.py`](example_1.py))

```python
from unittest.mock import Mock, MagicMock

payment = Mock()
payment.charge.return_value = {"status": "ok", "id": "txn_1"}
print(payment.charge(500, currency="INR"))
payment.charge.assert_called_once_with(500, currency="INR")
print("calls:", payment.charge.call_args_list)

flaky = Mock(side_effect=[ConnectionError("down"), "success"])
for _ in range(2):
    try:
        print(flaky())
    except ConnectionError as e:
        print("raised:", e)

m = MagicMock()
m.__len__.return_value = 3
m.__getitem__.side_effect = lambda k: k * 2
print(len(m), m[21])
```

### Example 2: patch: replacing network calls in tests  ([`example_2.py`](example_2.py))

```python
import unittest
from unittest.mock import patch
import urllib.request, json

def get_weather(city):
    with urllib.request.urlopen(f"https://api.weather.example/{city}") as r:
        data = json.loads(r.read())
    return f"{city}: {data['temp']}°C"

class TestWeather(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_weather(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = b'{"temp": 22}'
        self.assertEqual(get_weather("Kurukshetra"), "Kurukshetra: 22°C")
        mock_urlopen.assert_called_once()

    def test_time_freeze(self):
        with patch("time.time", return_value=1_700_000_000):
            import time
            self.assertEqual(time.time(), 1_700_000_000)

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

### Example 3: autospec and monkey patching  ([`example_3.py`](example_3.py))

```python
from unittest.mock import create_autospec, patch
import random

class EmailService:
    def send(self, to: str, subject: str, body: str) -> bool: ...

fake = create_autospec(EmailService, instance=True)
fake.send("a@b.com", "Hi", "Hello")
try:
    fake.send("only-one-arg")            # autospec catches calls with the wrong signature
except TypeError as e:
    print("autospec caught:", e)

def roll_dice():
    return random.randint(1, 6)

with patch.object(random, "randint", return_value=6):
    print("rigged dice:", [roll_dice() for _ in range(3)])
print("normal dice is back:", 1 <= roll_dice() <= 6)

class Greeter:
    def hello(self): return "hello"
original = Greeter.hello
Greeter.hello = lambda self: "monkey-patched hello!"
print(Greeter().hello())
Greeter.hello = original
print(Greeter().hello())
```

## Practice

1. Test a function that sends emails without sending any (mock the SMTP client).
2. Freeze `datetime.now()` in a test (hint: patch the module where it's looked up).
3. Use `side_effect` to test retry logic.

---

[⬅ Day 117](../Day-117-The-Buffer-Protocol-and-memoryview/README.md) · [🏠 Home](../README.md) · [Day 119 ➡](../Day-119-Modern-Python-Features-3-10-to-3-13/README.md)
