# 061 · collections Module — Example 1: Counter and defaultdict
# Run: python example_1.py

from collections import Counter, defaultdict

words = "to be or not to be that is the question to be".split()
c = Counter(words)
print(c.most_common(3))
print(Counter("mississippi"))
print(Counter(a=3, b=1) + Counter(a=1, b=2))

by_letter = defaultdict(list)
for w in words:
    by_letter[w[0]].append(w)
print(dict(by_letter))
graph = defaultdict(set)
graph["A"].add("B")
print(graph)
