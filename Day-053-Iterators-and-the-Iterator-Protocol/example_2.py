# Day 053 · Iterators and the Iterator Protocol — A custom iterator class
# Run: python example_2.py

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(5):
    print(n, end=" ")
print()
c = Countdown(2)
print(list(c), list(c), "<- exhausted the second time")
