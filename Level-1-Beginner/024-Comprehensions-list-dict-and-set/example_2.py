# 024 · Comprehensions: list, dict and set — Example 2: Dict and set comprehensions
# Run: python example_2.py

names = ["asha", "ravi", "meera"]
name_len = {n: len(n) for n in names}
print(name_len)
prices = {"pen": 10, "book": 250, "bag": 900}
expensive = {k: v for k, v in prices.items() if v > 100}
print(expensive)
unique_lengths = {len(n) for n in names}
print(unique_lengths)
