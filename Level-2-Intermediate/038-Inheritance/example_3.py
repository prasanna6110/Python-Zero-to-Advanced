# 038 · Inheritance — Example 3: Hierarchical inheritance: employees
# Run: python example_3.py

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
