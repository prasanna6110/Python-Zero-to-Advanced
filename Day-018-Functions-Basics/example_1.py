# Day 018 · Functions Basics — Defining and calling
# Run: python example_1.py

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Ananya"))
print(greet("Rahul"))
print(greet.__doc__)
