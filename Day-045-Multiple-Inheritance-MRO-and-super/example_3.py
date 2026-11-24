# Day 045 · Multiple Inheritance, MRO and super() — Mixins
# Run: python example_3.py

import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class ReprMixin:
    def __repr__(self):
        fields = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}({fields})"

class Product(JsonMixin, ReprMixin):
    def __init__(self, name, price):
        self.name, self.price = name, price

p = Product("Laptop", 55000)
print(p)
print(p.to_json())
