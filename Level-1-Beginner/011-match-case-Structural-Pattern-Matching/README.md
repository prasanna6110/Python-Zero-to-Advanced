# 011 · match-case (Structural Pattern Matching)

## match-case (Python 3.10+)
This is like `switch` in other languages, but far more powerful.

```python
match value:
    case 1:
        ...
    case 2 | 3:          # OR pattern
        ...
    case _:              # default (wildcard)
        ...
```

## Patterns you can match
- **Literals**: `case 404:`
- **OR patterns**: `case "y" | "yes":`
- **Capture variables**: `case x:` (the value is stored in `x`)
- **Guards**: `case x if x > 0:`
- **Sequences**: `case [x, y]:`, `case [first, *rest]:`
- **Mappings**: `case {"type": "click", "pos": p}:`
- **Class patterns**: `case Point(x=0, y=0):`

## Examples

### Example 1: Basic match  ([`example_1.py`](example_1.py))

```python
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 301 | 302:
            return "Redirect"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

for c in [200, 302, 404, 999]:
    print(c, "->", http_status(c))
```

### Example 2: Guards and capture  ([`example_2.py`](example_2.py))

```python
def classify(n):
    match n:
        case 0:
            return "zero"
        case x if x < 0:
            return f"negative ({x})"
        case x if x % 2 == 0:
            return f"positive even ({x})"
        case x:
            return f"positive odd ({x})"

for n in [0, -3, 8, 7]:
    print(classify(n))
```

### Example 3: Matching sequences and dicts  ([`example_3.py`](example_3.py))

```python
def handle(command):
    match command.split():
        case ["go", direction]:
            return f"Going {direction}"
        case ["pick", "up", item]:
            return f"Picked up {item}"
        case ["quit" | "exit"]:
            return "Bye!"
        case [first, *rest]:
            return f"Unknown command {first!r} with args {rest}"

for cmd in ["go north", "pick up sword", "exit", "dance fast now"]:
    print(handle(cmd))

event = {"type": "click", "x": 10, "y": 20}
match event:
    case {"type": "click", "x": x, "y": y}:
        print(f"Clicked at ({x}, {y})")
    case {"type": "key", "key": k}:
        print("Key pressed:", k)
```

## Practice

1. Write a calculator that uses `match` on the operator (`+ - * /`).
2. Match a tuple `(x, y)` and print whether the point is at the origin, on an axis or elsewhere.
3. Write a menu-driven program with `match` (1 = add, 2 = view, 3 = exit).

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
