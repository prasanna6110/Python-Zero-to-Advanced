# Day 080 · Descriptors — A typed field system (a mini ORM)
# Run: python example_2.py

class Field:
    def __init__(self, kind, required=True):
        self.kind, self.required = kind, required
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, obj, objtype=None):
        return self if obj is None else obj.__dict__.get(self.name)
    def __set__(self, obj, value):
        if value is None and not self.required:
            obj.__dict__[self.name] = None
            return
        if not isinstance(value, self.kind):
            raise TypeError(f"{self.name} must be {self.kind.__name__}, got {type(value).__name__}")
        obj.__dict__[self.name] = value

class User:
    name = Field(str)
    age = Field(int)
    email = Field(str, required=False)
    def __init__(self, name, age, email=None):
        self.name, self.age, self.email = name, age, email

u = User("Prasanna", 28)
print(u.name, u.age, u.email)
try:
    User("X", "twenty")
except TypeError as e:
    print("TypeError:", e)
