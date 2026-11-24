# Day 080 · Descriptors — A reusable validated field
# Run: python example_1.py

class Positive:
    def __set_name__(self, owner, name):
        self.private = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.private[1:]} must be positive, got {value}")
        setattr(obj, self.private, value)

class Product:
    price = Positive()
    quantity = Positive()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

p = Product(99.5, 3)
print(p.price, p.quantity)
try:
    p.quantity = -1
except ValueError as e:
    print("Error:", e)
