# 060 · Regular Expressions (re)

## Regular expressions
Patterns that **search, match and change text**.

## Core syntax
| Pattern | Meaning |
|---------|---------|
| `.` | any character except a newline |
| `\d \w \s` | digit, word character, whitespace (uppercase versions mean "not") |
| `[abc]`, `[a-z]`, `[^0-9]` | character classes |
| `* + ? {n} {n,m}` | quantifiers |
| `*? +?` | lazy (non-greedy) quantifiers |
| `^ $ \b` | start, end, word boundary |
| `( )` `(?P<name> )` `(?: )` | groups, named groups, non-capturing groups |
| `a\|b` | alternation |
| `(?=...)` `(?!...)` | lookahead |

## Functions
`re.search`, `re.match` (only at the start), `re.fullmatch`, `re.findall`, `re.finditer`, `re.sub`, `re.split`, `re.compile`

Always write patterns as **raw strings**: `r"\d+"`.

## Examples

### Example 1: search, findall, sub  ([`example_1.py`](example_1.py))

```python
import re

text = "Call 98765-43210 or 91234-56789. Email: prasanna@nitkkr.ac.in, help@site.com"
print(re.findall(r"\d{5}-\d{5}", text))
print(re.findall(r"[\w.]+@[\w.]+\.\w+", text))
m = re.search(r"(\d{5})-(\d{5})", text)
print(m.group(), m.group(1), m.span())
print(re.sub(r"\d{5}-\d{5}", "XXXXX-XXXXX", text))
print(re.split(r"[,.\s]+", "a, b. c  d"))
```

### Example 2: Named groups and parsing logs  ([`example_2.py`](example_2.py))

```python
import re

LOG = re.compile(
    r"(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>[^\]]+)\] \"(?P<method>GET|POST) (?P<path>\S+)\" (?P<status>\d{3})"
)
lines = [
    '10.0.0.1 - [24/Nov/2026:10:00:01] "GET /index.html" 200',
    '10.0.0.2 - [24/Nov/2026:10:00:05] "POST /login" 401',
]
for line in lines:
    m = LOG.search(line)
    if m:
        d = m.groupdict()
        print(d["ip"], d["method"], d["path"], d["status"])
```

### Example 3: Validation with fullmatch and lookahead  ([`example_3.py`](example_3.py))

```python
import re

def strong_password(p):
    return bool(re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%!]).{8,}", p))

for pw in ["password", "Passw0rd", "Passw0rd!", "Ab1!"]:
    print(f"{pw:<10} strong={strong_password(pw)}")

def valid_pan(pan):          # Indian PAN format: ABCDE1234F
    return re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan) is not None
print(valid_pan("ABCDE1234F"), valid_pan("abcde1234f"))
print(re.sub(r"(\w+)@(\w+)", r"\2 at \1", "user@domain"))
```

## Practice

1. Pull every hashtag out of a tweet.
2. Validate Indian mobile numbers (10 digits, starting with 6–9).
3. Convert dates from `DD-MM-YYYY` to `YYYY/MM/DD` using `re.sub` with groups.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
