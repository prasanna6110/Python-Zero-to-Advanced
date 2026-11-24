# 035 · Classes and Objects — Example 1: First class
# Run: python example_1.py

class Dog:
    def bark(self):
        print("Woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
print(type(d1), isinstance(d1, Dog), d1 is d2)
