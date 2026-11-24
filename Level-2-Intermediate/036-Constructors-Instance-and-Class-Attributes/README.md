# 036 · Constructors, Instance and Class Attributes

## `__init__`: the initializer (often called the constructor)
It runs automatically when an object is created and sets the object's starting state.

## Instance vs class attributes
| | Instance attribute | Class attribute |
|--|--------------------|-----------------|
| Defined | `self.x = ...` in methods | directly in the class body |
| Shared? | no, each object has its own | yes, shared by all objects |
| Use | per-object data | constants, counters, defaults |

⚠️ If you assign `obj.class_attr = value`, you create a new *instance* attribute that **hides** the class attribute. It doesn't change the class.

⚠️ Avoid **mutable** class attributes (like a list) unless you really want every object to share them.

## Examples

### Example 1: Instance vs class attributes  ([`example_1.py`](example_1.py))

```python
class Employee:
    company = "TechCorp"        # class attribute
    count = 0

    def __init__(self, name, salary):
        self.name = name        # instance attributes
        self.salary = salary
        Employee.count += 1

e1 = Employee("Ravi", 50000)
e2 = Employee("Sara", 65000)
print(e1.company, e2.company, Employee.count)
Employee.company = "NewCorp"
print(e1.company, e2.company)
```

### Example 2: Shadowing a class attribute  ([`example_2.py`](example_2.py))

```python
class Config:
    debug = False

a = Config()
b = Config()
a.debug = True               # creates an instance attribute on a only
print(a.debug, b.debug, Config.debug)
print(a.__dict__, b.__dict__)
```

### Example 3: The shared mutable class attribute bug  ([`example_3.py`](example_3.py))

```python
class BadTeam:
    members = []             # shared by ALL teams!
    def add(self, name):
        self.members.append(name)

class GoodTeam:
    def __init__(self):
        self.members = []    # each team gets its own list
    def add(self, name):
        self.members.append(name)

t1, t2 = BadTeam(), BadTeam()
t1.add("Asha")
print("BadTeam t2:", t2.members)
g1, g2 = GoodTeam(), GoodTeam()
g1.add("Asha")
print("GoodTeam g2:", g2.members)
```

## Practice

1. Count how many `Car` objects have been created using a class attribute.
2. Give each object a unique ID using a class-level counter.
3. Explain the output of Example 2.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
