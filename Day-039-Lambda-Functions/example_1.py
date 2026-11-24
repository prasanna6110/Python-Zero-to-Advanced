# Day 039 · Lambda Functions — Basic lambdas
# Run: python example_1.py

add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0
greet = lambda name="Guest": f"Hi {name}"
print(add(3, 4), is_even(10), greet(), greet("Zara"))
print((lambda x: x ** 3)(4))      # call it immediately
