# 037 · Instance, Class and Static Methods — Example 1: All three side by side
# Run: python example_1.py

class Pizza:
    base_price = 200

    def __init__(self, toppings):
        self.toppings = toppings

    def price(self):                       # instance method
        return self.base_price + 50 * len(self.toppings)

    @classmethod
    def margherita(cls):                   # alternative constructor
        return cls(["cheese", "tomato"])

    @staticmethod
    def is_veg(topping):                   # helper
        return topping not in {"chicken", "pepperoni"}

p = Pizza.margherita()
print(p.toppings, p.price())
print(Pizza.is_veg("chicken"), Pizza.is_veg("olive"))
