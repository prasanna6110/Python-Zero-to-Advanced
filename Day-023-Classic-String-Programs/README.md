# Day 023 · Classic String Programs

_Beginner_

## String programs that come up again and again
- Reverse a string or its words
- Palindrome and anagram checks
- Count vowels, consonants, digits and spaces
- Character frequency, plus the first non-repeating character
- Remove duplicates while keeping the order
- Capitalise each word, toggle case
- Check for a pangram (every letter a–z)
- Longest word, word count
- Compress a string: `"aaabb"` becomes `"a3b2"`
- Check whether one string is a rotation of another

**Tip:** strings are immutable, so to build a new one, collect the pieces in a **list** and `"".join(...)` it at the end.

## Examples

### Example 1: Reverse, palindrome, anagram and pangram  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: Counting characters and finding the first unique one  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Compression, rotation, title case and the longest word  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Count how many times each word appears in a paragraph.
2. Find all the permutations of a string without using itertools.
3. Check whether a string has balanced brackets: `({[]})`.
4. Find the longest palindromic substring.

---

[⬅ Day 022](../Day-022-Classic-Number-Programs-Exam-and-Interview-Favourites/README.md) · [🏠 Home](../README.md) · [Day 024 ➡](../Day-024-Lists/README.md)
