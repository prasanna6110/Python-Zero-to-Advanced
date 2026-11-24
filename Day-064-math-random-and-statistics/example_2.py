# Day 064 · math, random and statistics — random module
# Run: python example_2.py

import random

random.seed(42)          # reproducible results
print(random.randint(1, 6), random.random(), random.uniform(1, 10))
colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors))
print(random.sample(colors, 2))
print(random.choices(["win", "lose"], weights=[1, 9], k=10))
deck = list(range(1, 11))
random.shuffle(deck)
print(deck)
