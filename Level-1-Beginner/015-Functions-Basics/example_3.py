# 015 · Functions Basics — Example 3: Functions are objects
# Run: python example_3.py

def square(x):
    return x * x

def cube(x):
    return x ** 3

operations = {"square": square, "cube": cube}
for name, func in operations.items():
    print(name, func(3))

f = square            # assign a function to a variable
print(f(9), f.__name__)
