# 046 · Iterators and the Iterator Protocol — Example 3: A reusable iterable (separate iterator object)
# Run: python example_3.py

class Range2:
    """Iterable that can be looped over many times."""
    def __init__(self, start, stop, step=1):
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        current = self.start
        while current < self.stop:
            yield current          # a generator makes a fresh iterator each time
            current += self.step

r = Range2(0, 10, 3)
print(list(r), list(r))
print(sum(r), max(r))
