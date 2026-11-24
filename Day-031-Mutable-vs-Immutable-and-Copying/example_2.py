# Day 031 · Mutable vs Immutable and Copying — Functions can change mutable arguments
# Run: python example_2.py

def add_item(cart, item):
    cart.append(item)

def change_number(n):
    n += 100
    return n

my_cart = ["milk"]
add_item(my_cart, "bread")
print(my_cart)          # changed!

x = 5
change_number(x)
print(x)                # unchanged: ints are immutable
