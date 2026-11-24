# 107 · Advanced Structural Pattern Matching

## Beyond the basics
| Pattern | Example |
|---------|---------|
| Class pattern (keyword) | `case Point(x=0, y=y):` |
| Class pattern (positional) | `case Point(0, y):`, which needs `__match_args__` |
| Built-in type patterns | `case int(n) \| float(n):`, `case str() as s:` |
| Nested | `case {"user": {"roles": [*_, "admin", *_]}}:` (⚠️ a star can appear only once per sequence) |
| `as` capture | `case [Point() as p, *rest]:` |
| Value pattern | `case Color.RED:` (dotted names are constants) |
| Guards | `case Order(total=t) if t > 1000:` |

## How it works
- A dataclass sets `__match_args__` automatically.
- Mapping patterns match **partially**: extra keys are fine. Use `**rest` to capture them.
- A bare name always **captures** the value. To compare against a constant, write a dotted name such as `Color.RED`.

Pattern matching shines at parsing commands, handling JSON or API events, walking ASTs and building interpreters.

## Examples

### Example 1: Class patterns with dataclasses  ([`example_1.py`](example_1.py))

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

def where(p):
    match p:
        case Point(0, 0):
            return "origin"
        case Point(0, y):
            return f"on the Y axis at {y}"
        case Point(x, 0):
            return f"on the X axis at {x}"
        case Point(x, y) if x == y:
            return f"on the diagonal at {x}"
        case Point():
            return f"somewhere ({p.x}, {p.y})"
        case _:
            return "not a point"

for p in [Point(0, 0), Point(0, 5), Point(3, 0), Point(4, 4), Point(1, 9), "x"]:
    print(p, "->", where(p))
print(Point.__match_args__)
```

### Example 2: Matching nested JSON events  ([`example_2.py`](example_2.py))

```python
events = [
    {"type": "push", "repo": "course", "commits": [{"msg": "add day 1"}, {"msg": "fix typo"}]},
    {"type": "issue", "action": "opened", "user": {"login": "asha", "roles": ["member", "admin"]}},
    {"type": "issue", "action": "closed", "user": {"login": "ravi", "roles": ["member"]}},
    {"type": "star", "count": 1000, "extra": "ignored"},
    {"type": "unknown"},
]

def handle(event):
    match event:
        case {"type": "push", "commits": [{"msg": first}, *rest]}:
            return f"push: '{first}' + {len(rest)} more commits"
        case {"type": "issue", "action": "opened", "user": {"login": login, "roles": [*roles]}} if "admin" in roles:
            return f"issue opened by admin {login}"
        case {"type": "issue", "action": action, "user": {"login": login}}:
            return f"issue {action} by {login}"
        case {"type": "star", "count": int(n), **rest} if n >= 1000:
            return f"milestone: {n} stars! (other keys: {list(rest)})"
        case {"type": t}:
            return f"unhandled event type {t!r}"

for e in events:
    print(handle(e))
```

### Example 3: A tiny expression evaluator using matching  ([`example_3.py`](example_3.py))

```python
from dataclasses import dataclass

@dataclass
class Num:
    value: float
@dataclass
class BinOp:
    op: str
    left: object
    right: object
@dataclass
class Neg:
    operand: object

def evaluate(node):
    match node:
        case Num(v):
            return v
        case Neg(operand):
            return -evaluate(operand)
        case BinOp("+", l, r): return evaluate(l) + evaluate(r)
        case BinOp("-", l, r): return evaluate(l) - evaluate(r)
        case BinOp("*", l, r): return evaluate(l) * evaluate(r)
        case BinOp("/", l, Num(0)): raise ZeroDivisionError("division by literal zero")
        case BinOp("/", l, r): return evaluate(l) / evaluate(r)
        case _: raise ValueError(f"bad node {node}")

def simplify(node):
    match node:
        case BinOp("*", x, Num(1)) | BinOp("*", Num(1), x): return simplify(x)
        case BinOp("+", x, Num(0)) | BinOp("+", Num(0), x): return simplify(x)
        case BinOp(op, l, r): return BinOp(op, simplify(l), simplify(r))
        case _: return node

expr = BinOp("+", BinOp("*", Num(4), Num(1)), Neg(BinOp("+", Num(2), Num(0))))
print(evaluate(expr), "| simplified:", simplify(expr))
```

## Practice

1. Write a JSON-schema-like validator using mapping patterns.
2. Write a text-adventure command parser with sequence patterns.
3. Add `__match_args__` to a normal (non-dataclass) class and match it positionally.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
