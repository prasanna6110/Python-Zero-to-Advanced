# Day 055 · Closures — Closures that keep state
# Run: python example_2.py

def make_averager():
    numbers = []
    def add(n):
        numbers.append(n)
        return sum(numbers) / len(numbers)
    return add

avg = make_averager()
print(avg(10), avg(20), avg(60))

def power_factory(exp):
    return lambda base: base ** exp
square, cube = power_factory(2), power_factory(3)
print(square(5), cube(5))
