# Day 023 · Classic String Programs — Compression, rotation, title case and the longest word
# Run: python example_3.py

from itertools import groupby

def compress(s):
    return "".join(f"{ch}{len(list(g))}" for ch, g in groupby(s))

def is_rotation(a, b):
    return len(a) == len(b) and b in a + a

def my_title(s):
    return " ".join(w[:1].upper() + w[1:].lower() for w in s.split())

sentence = "the quick brown fox jumped over extraordinary obstacles"
print(compress("aaabbbcccd"), compress("wwwwaaadexxxxxx"))
print(is_rotation("waterbottle", "erbottlewat"), is_rotation("abc", "acb"))
print(my_title("hELLO wORLD from pYTHON"))
print("longest word:", max(sentence.split(), key=len))
print("toggle case:", "PyThOn".swapcase())
print("word count:", len(sentence.split()))
