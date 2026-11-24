# 017 · Scope: LEGB, global and nonlocal — Example 2: global keyword
# Run: python example_2.py

counter = 0

def increment():
    global counter
    counter += 1

for _ in range(5):
    increment()
print("counter =", counter)
