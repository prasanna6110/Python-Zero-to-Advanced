# Day 096 · Functional Programming in Python — Pure vs impure and immutability
# Run: python example_1.py

total = 0
def impure_add(x):            # changes outside state
    global total
    total += x
    return total

def pure_add(a, b):           # depends only on its inputs
    return a + b

print(impure_add(5), impure_add(5), "<- same input, different output")
print(pure_add(5, 5), pure_add(5, 5))

prices = (100, 200, 300)                       # immutable tuple
discounted = tuple(p * 0.9 for p in prices)    # a new tuple, the original is safe
print(prices, discounted)
