# Day 020 · Scope: LEGB, global and nonlocal — nonlocal keyword
# Run: python example_3.py

def make_counter():
    count = 0
    def step():
        nonlocal count
        count += 1
        return count
    return step

c = make_counter()
print(c(), c(), c())
c2 = make_counter()
print(c2())    # each counter keeps its own state
