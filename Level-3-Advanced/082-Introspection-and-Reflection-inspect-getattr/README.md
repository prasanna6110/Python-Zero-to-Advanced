# 082 · Introspection and Reflection (inspect, getattr)

## Introspection: examining objects while the program runs
`type, isinstance, dir, vars, id, callable, hasattr, getattr, setattr, delattr, __dict__, __class__, __module__, __qualname__`

## Reflection: changing behaviour based on names known only at runtime
`getattr(obj, "method_name")()` calls a method chosen by a string. It's useful for plugins, CLIs and dispatchers.

## The inspect module
| Function | Gives |
|----------|-------|
| `inspect.signature(f)` | parameters and annotations |
| `inspect.getsource(f)` | source code |
| `inspect.getmembers(obj, predicate)` | members |
| `inspect.isfunction / isclass / iscoroutinefunction` | type checks |
| `inspect.stack()` / `currentframe()` | the call stack |
| `inspect.getdoc`, `getfile` | documentation and file |

## Examples

### Example 1: dir, vars, getattr and setattr  ([`example_1.py`](example_1.py))

```python
class Robot:
    def __init__(self):
        self.name = "R2"
        self.battery = 80
    def walk(self): return "walking"
    def talk(self): return "beep"

r = Robot()
print([m for m in dir(r) if not m.startswith("_")])
print(vars(r))
for action in ["walk", "talk", "fly"]:
    method = getattr(r, action, None)
    print(action, "->", method() if callable(method) else "not supported")
setattr(r, "battery", 100)
print(r.battery, hasattr(r, "name"))
```

### Example 2: inspect.signature for automatic validation  ([`example_2.py`](example_2.py))

```python
import inspect

def create_user(name: str, age: int, active: bool = True) -> dict:
    """Create a user record."""
    return {"name": name, "age": age, "active": active}

sig = inspect.signature(create_user)
print(sig)
for p in sig.parameters.values():
    print(f"  {p.name}: {p.annotation.__name__}, default={p.default if p.default is not p.empty else '-'}")

bound = sig.bind("Asha", 21)
bound.apply_defaults()
print(bound.arguments)
print(inspect.getdoc(create_user), "| source lines:", len(inspect.getsource(create_user).splitlines()))
```

### Example 3: The call stack and a command dispatcher  ([`example_3.py`](example_3.py))

```python
import inspect

def who_called_me():
    caller = inspect.stack()[1]
    return f"called from {caller.function}() at line {caller.lineno}"

def report():
    print(who_called_me())

report()

class Shell:
    def do_hello(self, arg): return f"Hello {arg}"
    def do_add(self, arg): return sum(map(int, arg.split()))
    def run(self, line):
        cmd, _, arg = line.partition(" ")
        handler = getattr(self, f"do_{cmd}", None)
        return handler(arg) if handler else f"unknown: {cmd}"

sh = Shell()
for line in ["hello world", "add 1 2 3", "jump"]:
    print(line, "=>", sh.run(line))
commands = [n[3:] for n, _ in inspect.getmembers(sh, inspect.ismethod) if n.startswith("do_")]
print("available commands:", commands)
```

## Practice

1. Write a function that prints every method of any object together with its signature.
2. Write a decorator that checks argument types using `inspect.signature`.
3. Build a mini CLI where each `do_*` method becomes a command.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
