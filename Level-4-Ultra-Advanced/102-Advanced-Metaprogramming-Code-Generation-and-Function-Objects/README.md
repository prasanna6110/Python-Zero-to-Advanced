# 102 · Advanced Metaprogramming: Code Generation and Function Objects

## Tools for generating code while the program runs
| Tool | Use |
|------|-----|
| `type(name, bases, dict)` | create classes |
| `types.FunctionType(code, globals, name, defaults, closure)` | build functions from code objects |
| `func.__code__.replace(...)` (3.8+) | change a function's code object |
| `exec(src, namespace)` | generate source code and run it (how `dataclasses` and `namedtuple` work!) |
| `types.SimpleNamespace`, `types.MappingProxyType` | lightweight objects, read-only dict views |
| `__getattr__` on a module (PEP 562) | lazy attributes or deprecation warnings for a module |
| `sys._getframe()` | access call frames |

## ⚠️ Rules for exec and eval
Never pass them **untrusted** input. Build the source from strings you control, and always give them an explicit namespace dict.

## Examples

### Example 1: Generating a record class with exec (how namedtuple works)  ([`example_1.py`](example_1.py))

```python
def make_record(name, fields):
    args = ", ".join(fields)
    assigns = "\n".join(f"        self.{f} = {f}" for f in fields) or "        pass"
    reprs = ", ".join(f"{f}={{self.{f}!r}}" for f in fields)
    src = f"""
class {name}:
    __slots__ = {tuple(fields)!r}
    def __init__(self, {args}):
{assigns}
    def __repr__(self):
        return f"{name}({reprs})"
    def __eq__(self, other):
        return all(getattr(self, f) == getattr(other, f) for f in self.__slots__)
"""
    namespace = {}
    exec(src, namespace)
    cls = namespace[name]
    cls._source = src
    return cls

Student = make_record("Student", ["name", "roll", "cgpa"])
s = Student("Asha", 101, 9.1)
print(s, s == Student("Asha", 101, 9.1))
print(Student._source)
```

### Example 2: Building and modifying functions with code objects  ([`example_2.py`](example_2.py))

```python
import types

def template(x):
    return x + 1

code = template.__code__
new_code = code.replace(co_consts=tuple(10 if c == 1 else c for c in code.co_consts))
add_ten = types.FunctionType(new_code, globals(), "add_ten")
print(template(5), add_ten(5))

def make_adder(n):
    def adder(x): return x + n
    return adder
a5 = make_adder(5)
clone = types.FunctionType(a5.__code__, a5.__globals__, "clone", None, a5.__closure__)
print("cloned closure:", clone(100), "| closure value:", a5.__closure__[0].cell_contents)

ns = types.SimpleNamespace(host="localhost", port=8000)
ns.debug = True
print(ns)
ro = types.MappingProxyType({"a": 1})
try:
    ro["b"] = 2
except TypeError as e:
    print("read-only mapping:", e)
```

### Example 3: Module __getattr__ and a dynamic API client  ([`example_3.py`](example_3.py))

```python
import sys, types, warnings

mod = types.ModuleType("config_mod")
exec('''
import warnings
_settings = {"timeout": 30, "retries": 3}
def __getattr__(name):
    if name == "TIMEOUT_OLD":
        warnings.warn("TIMEOUT_OLD is deprecated, use timeout", DeprecationWarning)
        return _settings["timeout"]
    if name in _settings:
        return _settings[name]
    raise AttributeError(f"module has no attribute {name!r}")
''', mod.__dict__)
sys.modules["config_mod"] = mod
import config_mod
print(config_mod.timeout, config_mod.retries)
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    print(config_mod.TIMEOUT_OLD, "| warning:", w[0].message)

class APIClient:
    """Any attribute chain becomes a URL path: client.users.list() -> GET /users/list"""
    def __init__(self, path=""):
        self._path = path
    def __getattr__(self, name):
        return APIClient(f"{self._path}/{name}")
    def __call__(self, **params):
        q = "&".join(f"{k}={v}" for k, v in params.items())
        return f"GET {self._path}" + (f"?{q}" if q else "")

api = APIClient()
print(api.users.list(page=2))
print(api.repos.prasanna6110.issues())
```

## Practice

1. Write `make_validator(schema)` that generates a validation function using exec.
2. Write a "fluent" query builder using `__getattr__`.
3. Use module-level `__getattr__` to lazily import a heavy submodule.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
