# Day 081 · Metaclasses — type() creates classes
# Run: python example_1.py

def speak(self):
    return f"{self.name} speaks"

Animal = type("Animal", (), {"name": "generic", "speak": speak})
Dog = type("Dog", (Animal,), {"name": "dog"})

print(Dog().speak(), Dog.__mro__)
print(type(Dog), type(type))
