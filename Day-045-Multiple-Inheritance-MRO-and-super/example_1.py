# Day 045 · Multiple Inheritance, MRO and super() — Basic multiple inheritance
# Run: python example_1.py

class Flyer:
    def fly(self):
        return "flying"

class Swimmer:
    def swim(self):
        return "swimming"

class Duck(Flyer, Swimmer):
    pass

d = Duck()
print(d.fly(), d.swim())
print([c.__name__ for c in Duck.__mro__])
