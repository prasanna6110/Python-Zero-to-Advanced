# Day 126 · Writing Pythonic Code (Idioms and Best Practices) — Handy idioms worth memorising
# Run: python example_3.py

from collections import Counter, defaultdict

words = "the cat sat on the mat the end".split()
print(Counter(words).most_common(1))
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)
print(dict(groups))
print(max(words, key=len), sorted(words, key=len)[:3])
print(dict(zip(["a", "b"], [1, 2])), {v: k for k, v in {"a": 1}.items()})
first, *_, last = words
print(first, last, "|", *reversed(words[:3]))
print(" ".join(f"{i}:{w}" for i, w in enumerate(words[:3], 1)))
with open(__file__) as f:
    print("this file has", sum(1 for _ in f), "lines")
