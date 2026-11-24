# 038 · Inheritance

## Inheritance
A **child class** gets the attributes and methods of a **parent class**, and can add to them or **override** them.
```python
class Child(Parent):
    ...
```
- `super()` calls the parent's version of a method, most often `__init__`.
- **Method overriding**: the child defines a method with the same name as the parent's.
- `isinstance(obj, Parent)` is True for child objects too.
- `issubclass(Child, Parent)` checks the relationship between classes.

## Types of inheritance
Single, multilevel (A → B → C), hierarchical (one parent with many children) and multiple (covered in the next topic).

## Examples

### Example 1: Single inheritance and super()  ([`example_1.py`](example_1.py))

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof"

d = Dog("Tommy", "Labrador")
print(d.describe(), "|", d.breed)
print(isinstance(d, Animal), issubclass(Dog, Animal))
```

### Example 2: Multilevel inheritance  ([`example_2.py`](example_2.py))

```python
class Vehicle:
    def start(self):
        return "Engine started"

class Car(Vehicle):
    wheels = 4
    def drive(self):
        return "Driving"

class ElectricCar(Car):
    def start(self):
        return "Silent start ⚡ (" + super().start() + ")"

tesla = ElectricCar()
print(tesla.start(), tesla.drive(), tesla.wheels)
print(ElectricCar.__mro__)
```

### Example 3: Hierarchical inheritance: employees  ([`example_3.py`](example_3.py))

```python
class Employee:
    def __init__(self, name, base):
        self.name, self.base = name, base
    def salary(self):
        return self.base

class Manager(Employee):
    def salary(self):
        return self.base * 1.5

class Intern(Employee):
    def salary(self):
        return self.base * 0.5

for e in [Employee("A", 40000), Manager("B", 40000), Intern("C", 40000)]:
    print(f"{type(e).__name__:<9} {e.name}: ₹{e.salary():,.0f}")
```

## Practice

1. Create `Shape` → `Circle` and `Square`, each with its own `area()`.
2. Build `Person` → `Student` → `GraduateStudent` (multilevel).
3. Override `__str__` in a child class and call the parent's version with `super()`.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
