# 072 · __init_subclass__, __class_getitem__ and Class Creation Hooks

## `__init_subclass__` (3.6+): a lightweight alternative to metaclasses
It's called on the **parent** whenever a subclass is created.
```python
class Base:
    def __init_subclass__(cls, /, **kwargs):
        super().__init_subclass__(**kwargs)
        ...
class Child(Base, key="value"): ...     # class keyword arguments arrive as kwargs
```
## `__class_getitem__`
It makes `MyClass[int]` work. That's how generics are written (`list[int]`).

## Other hooks
| Hook | When it runs |
|------|--------------|
| `__set_name__` | a descriptor is assigned in a class body |
| `__init_subclass__` | a subclass is created |
| `__instancecheck__` / `__subclasscheck__` | `isinstance()` / `issubclass()` (defined on a metaclass) |
| `__mro_entries__` | an object that isn't a class is used as a base |

## Examples

### Example 1: A plugin registry with __init_subclass__  ([`example_1.py`](example_1.py))

```python
class Exporter:
    registry = {}

    def __init_subclass__(cls, /, fmt=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if fmt is None:
            raise TypeError(f"{cls.__name__} needs fmt=...")
        Exporter.registry[fmt] = cls

    @classmethod
    def for_format(cls, fmt):
        return cls.registry[fmt]()

class JSONExporter(Exporter, fmt="json"):
    def export(self, d): return str(d).replace("'", '"')

class XMLExporter(Exporter, fmt="xml"):
    def export(self, d): return "".join(f"<{k}>{v}</{k}>" for k, v in d.items())

data = {"name": "Asha", "age": 21}
for fmt in Exporter.registry:
    print(fmt, "->", Exporter.for_format(fmt).export(data))
```

### Example 2: Enforcing an interface on subclasses  ([`example_2.py`](example_2.py))

```python
class Command:
    required = ("execute", "undo")

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        missing = [m for m in cls.required if not callable(getattr(cls, m, None))]
        if missing:
            raise TypeError(f"{cls.__name__} is missing: {', '.join(missing)}")

class Paste(Command):
    def execute(self): return "pasted"
    def undo(self): return "unpasted"

print(Paste().execute())
try:
    class Cut(Command):
        def execute(self): ...
except TypeError as e:
    print("TypeError:", e)
```

### Example 3: __class_getitem__ and __instancecheck__  ([`example_3.py`](example_3.py))

```python
class TypedList(list):
    def __class_getitem__(cls, item_type):
        class Specialized(cls):
            def append(self, value):
                if not isinstance(value, item_type):
                    raise TypeError(f"expected {item_type.__name__}")
                super().append(value)
        Specialized.__name__ = f"TypedList[{item_type.__name__}]"
        return Specialized

IntList = TypedList[int]
nums = IntList()
nums.append(5)
try:
    nums.append("x")
except TypeError as e:
    print(IntList.__name__, "->", e)

class DuckCheck(type):
    def __instancecheck__(cls, obj):
        return hasattr(obj, "quack")

class Duckish(metaclass=DuckCheck): pass
class Robot:
    def quack(self): ...
print(isinstance(Robot(), Duckish), isinstance(42, Duckish))
```

## Practice

1. Use `__init_subclass__` to give every subclass an automatic `id` prefix.
2. Build `Matrix[float]` with `__class_getitem__`.
3. When would you still need a full metaclass instead of `__init_subclass__`?

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
