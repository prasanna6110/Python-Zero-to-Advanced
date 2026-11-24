# 036 · Constructors, Instance and Class Attributes — Example 2: Shadowing a class attribute
# Run: python example_2.py

class Config:
    debug = False

a = Config()
b = Config()
a.debug = True               # creates an instance attribute on a only
print(a.debug, b.debug, Config.debug)
print(a.__dict__, b.__dict__)
