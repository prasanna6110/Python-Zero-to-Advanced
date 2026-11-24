# 062 · itertools — Example 1: Infinite iterators and islice
# Run: python example_1.py

from itertools import count, cycle, repeat, islice

print(list(islice(count(10, 5), 5)))
print(list(islice(cycle("ABC"), 7)))
print(list(repeat("hi", 3)))
for turn, player in zip(range(1, 6), cycle(["Asha", "Ravi"])):
    print(f"Turn {turn}: {player}")
