# Day 047 · Polymorphism and Duck Typing — Duck typing
# Run: python example_2.py

class Duck:
    def speak(self): return "Quack"

class Robot:
    def speak(self): return "Beep boop"

class Person:
    def speak(self): return "Hello"

def make_it_speak(thing):       # no type checks at all
    print(thing.speak())

for obj in [Duck(), Robot(), Person()]:
    make_it_speak(obj)
