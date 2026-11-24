# Day 023 · Classic String Programs — Reverse, palindrome, anagram and pangram
# Run: python example_1.py

def is_palindrome(s):
    clean = "".join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

def is_anagram(a, b):
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())

def is_pangram(s):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())

text = "Python is fun to learn"
print(text[::-1])
print(" ".join(text.split()[::-1]))
print(" ".join(w[::-1] for w in text.split()))
print(is_palindrome("Never odd or even"), is_anagram("listen", "silent"), is_anagram("Dormitory", "dirty room"))
print(is_pangram("The quick brown fox jumps over the lazy dog"))
