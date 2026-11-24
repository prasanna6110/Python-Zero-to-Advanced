# Day 054 · Generators and yield — Memory: list vs generator
# Run: python example_2.py

import sys
squares_list = [x * x for x in range(1_000_000)]
squares_gen = (x * x for x in range(1_000_000))
print("list size :", sys.getsizeof(squares_list), "bytes")
print("gen size  :", sys.getsizeof(squares_gen), "bytes")
print("sum from gen:", sum(squares_gen))

def fibonacci():                # an infinite generator
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(12)])
