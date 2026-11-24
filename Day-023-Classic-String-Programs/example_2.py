# Day 023 · Classic String Programs — Counting characters and finding the first unique one
# Run: python example_2.py

from collections import Counter

s = "Programming in Python 3.13 is awesome!"
vowels = sum(c in "aeiouAEIOU" for c in s)
consonants = sum(c.isalpha() and c not in "aeiouAEIOU" for c in s)
digits = sum(c.isdigit() for c in s)
spaces = s.count(" ")
print(f"vowels={vowels} consonants={consonants} digits={digits} spaces={spaces}")

freq = Counter(s.lower().replace(" ", ""))
print("most common:", freq.most_common(3))

def first_unique(s):
    counts = Counter(s)
    return next((c for c in s if counts[c] == 1), None)
print("first non-repeating in 'swiss':", first_unique("swiss"))
print("remove duplicates:", "".join(dict.fromkeys("programming")))
