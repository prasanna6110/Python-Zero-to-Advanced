# Day 081 · Metaclasses

_Advanced_

## Classes are objects too
In Python **everything is an object, including classes**. The class of a class is called its **metaclass**. By default that's `type`.

```python
type(5)        # <class 'int'>
type(int)      # <class 'type'>
```
## Creating a class dynamically
```python
MyClass = type("MyClass", (Base,), {"x": 1, "hello": func})
```
## A custom metaclass
```python
class Meta(type):
    def __new__(mcls, name, bases, namespace):
        # inspect or change the class before it exists
        return super().__new__(mcls, name, bases, namespace)

class Model(metaclass=Meta): ...
```
Hooks you can define: `__prepare__` (sets up the namespace dict), `__new__`, `__init__` and `__call__` (which controls how **instances** are created).

## When to use them
Registries, enforcing rules on classes (interfaces, naming), ORMs and singletons.

> "Metaclasses are deeper magic than 99% of users should ever worry about." Try **decorators** or **`__init_subclass__`** first.

## Examples

### Example 1: type() creates classes  ([`example_1.py`](example_1.py))

```python
def speak(self):
    return f"{self.name} speaks"

Animal = type("Animal", (), {"name": "generic", "speak": speak})
Dog = type("Dog", (Animal,), {"name": "dog"})

print(Dog().speak(), Dog.__mro__)
print(type(Dog), type(type))
```

### Example 2: A metaclass that enforces rules and registers classes  ([`example_2.py`](example_2.py))

```python
class PluginMeta(type):
    registry = {}

    def __new__(mcls, name, bases, ns):
        cls = super().__new__(mcls, name, bases, ns)
        if bases:                                  # skip the base class itself
            if "run" not in ns:
                raise TypeError(f"{name} must define run()")
            mcls.registry[name.lower()] = cls
        return cls

class Plugin(metaclass=PluginMeta):
    pass

class Resize(Plugin):
    def run(self): return "resizing"

class Blur(Plugin):
    def run(self): return "blurring"

print(PluginMeta.registry)
print([cls().run() for cls in PluginMeta.registry.values()])
try:
    class Broken(Plugin):
        pass
except TypeError as e:
    print("TypeError:", e)
```

### Example 3: __call__ for singletons and __prepare__ for ordering  ([`example_3.py`](example_3.py))

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        print("  connecting once...")

print(Database() is Database())

class Recorder(type):
    @classmethod
    def __prepare__(mcls, name, bases):
        print(f"  preparing namespace for {name}")
        return {"created_by": "Recorder"}
    def __new__(mcls, name, bases, ns):
        ns["fields"] = [k for k in ns if not k.startswith("__") and k != "created_by"]
        return super().__new__(mcls, name, bases, ns)

class Form(metaclass=Recorder):
    username = str
    password = str

print(Form.fields, Form.created_by)
```

## Practice

1. Write a metaclass that turns all method names to lowercase.
2. Write a metaclass that stops a class from being subclassed (a "final" class).
3. Rewrite the plugin registry using `__init_subclass__` (next topic) and compare the two.

---

[⬅ Day 080](../Day-080-Descriptors/README.md) · [🏠 Home](../README.md) · [Day 082 ➡](../Day-082-init-subclass-class-getitem-and-Class-Creation-Hooks/README.md)
