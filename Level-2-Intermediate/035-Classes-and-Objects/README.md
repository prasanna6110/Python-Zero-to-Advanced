# 035 · Classes and Objects

## Object-Oriented Programming (OOP)
OOP organises code around **objects**, which bundle **data (attributes)** together with **behaviour (methods)**.

- A **class** is a blueprint (for example `Car`).
- An **object** or **instance** is one thing built from that blueprint (for example `my_car = Car()`).
- `self` refers to the current object and is always the first parameter of an instance method.

## The four pillars of OOP
1. **Encapsulation**: bundling data with methods and hiding the internal details.
2. **Inheritance**: reusing code from a parent class.
3. **Polymorphism**: the same interface behaving differently for different objects.
4. **Abstraction**: showing only what's essential.

## Examples

### Example 1: First class  ([`example_1.py`](example_1.py))

```python
class Dog:
    def bark(self):
        print("Woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
print(type(d1), isinstance(d1, Dog), d1 is d2)
```

### Example 2: Attributes and methods  ([`example_2.py`](example_2.py))

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def report(self):
        print(f"{self.name}: average {self.average():.1f}")

s = Student("Asha", [90, 85, 77])
s.report()
s.marks.append(100)
s.report()
print(vars(s))         # the object's attributes as a dict
```

### Example 3: Modelling a real thing: BankAccount  ([`example_3.py`](example_3.py))

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount
        self.history.append(("withdraw", amount))

acc = BankAccount("Prasanna", 1000)
acc.deposit(500)
acc.withdraw(2000)
acc.withdraw(300)
print(acc.owner, acc.balance, acc.history)
```

## Practice

1. Create a `Rectangle` class with `area()` and `perimeter()`.
2. Create a `Book` class and make a list of 3 books. Print the most expensive one.
3. Add a `transfer(other_account, amount)` method to BankAccount.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
