# Day 042 · Constructors, Instance and Class Attributes — Instance vs class attributes
# Run: python example_1.py

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
