# 040 · Encapsulation, Name Mangling and Properties — Example 2: Property with validation
# Run: python example_2.py

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
