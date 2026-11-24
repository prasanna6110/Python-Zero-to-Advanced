# 063 · functools — Example 2: cached_property
# Run: python example_2.py

from functools import cached_property

class Dataset:
    def __init__(self, numbers):
        self.numbers = numbers

    @cached_property
    def stats(self):
        print("  ...computing stats (only once)")
        n = len(self.numbers)
        mean = sum(self.numbers) / n
        var = sum((x - mean) ** 2 for x in self.numbers) / n
        return {"mean": mean, "std": var ** 0.5}

d = Dataset([2, 4, 4, 4, 5, 5, 7, 9])
print(d.stats)
print(d.stats)
