# Day 046 · Encapsulation, Name Mangling and Properties

_Intermediate_

## Access conventions (Python doesn't have strict private members)
| Name | Meaning |
|------|---------|
| `name` | public |
| `_name` | "protected": internal use, by convention only |
| `__name` | "private": **name mangling** turns it into `_ClassName__name` |

## Properties
`@property` lets you write a method that is **accessed like an attribute**. It's useful for:
- **validation** when a value is set
- **computed** attributes
- **read-only** attributes (a getter with no setter)

```python
@property
def age(self): return self._age

@age.setter
def age(self, value): ...
```

## Examples

### Example 1: Protected and private  ([`example_1.py`](example_1.py))

```python
class Account:
    def __init__(self, balance):
        self._bank = "SBI"          # protected (convention)
        self.__pin = 1234           # private (name-mangled)
        self.balance = balance

    def check_pin(self, pin):
        return pin == self.__pin

a = Account(500)
print(a._bank, a.check_pin(1234))
try:
    print(a.__pin)
except AttributeError as e:
    print("AttributeError:", e)
print("Mangled name still exists:", a._Account__pin)
```

### Example 2: Property with validation  ([`example_2.py`](example_2.py))

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age          # goes through the setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not 0 <= value <= 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

p = Person("Neha", 25)
p.age = 30
print(p.age)
try:
    p.age = -1
except ValueError as e:
    print("Error:", e)
```

### Example 3: Computed and read-only properties  ([`example_3.py`](example_3.py))

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, d):
        self.radius = d / 2

c = Circle(5)
print(c.area, c.diameter)
c.diameter = 20
print(c.radius, round(c.area, 2))
try:
    c.area = 100
except AttributeError as e:
    print("Read-only:", e)
```

## Practice

1. Make a `Temperature` class with a `celsius` property and a computed `fahrenheit` property.
2. Make `balance` read-only, so it can only change through deposit and withdraw.
3. Explain name mangling and why it exists (hint: it stops subclasses from clashing with names).

---

[⬅ Day 045](../Day-045-Multiple-Inheritance-MRO-and-super/README.md) · [🏠 Home](../README.md) · [Day 047 ➡](../Day-047-Polymorphism-and-Duck-Typing/README.md)
