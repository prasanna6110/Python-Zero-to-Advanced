# 047 · Generators and yield — Example 1: A simple generator
# Run: python example_1.py

def count_up_to(n):
    print("  (generator started)")
    i = 1
    while i <= n:
        yield i
        i += 1
    print("  (generator finished)")

gen = count_up_to(3)
print(type(gen))
print(next(gen))
print(next(gen))
for value in gen:
    print(value)
