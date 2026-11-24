# 038 · Inheritance — Example 1: Single inheritance and super()
# Run: python example_1.py

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
