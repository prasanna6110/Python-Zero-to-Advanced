# Day 020 · Scope: LEGB, global and nonlocal — global keyword
# Run: python example_2.py

counter = 0

def increment():
    global counter
    counter += 1

for _ in range(5):
    increment()
print("counter =", counter)
