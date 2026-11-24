# Day 009 · Strings Basics: Indexing and Slicing

_Beginner_

## Strings
A string is an **immutable sequence of characters**. You can write one with `'single'`, `"double"` or `'''triple'''` quotes (triple quotes allow multiple lines).

## Indexing
```
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```
`s[0]` gives `'P'` and `s[-1]` gives `'n'`.

## Slicing: `s[start:stop:step]`
- `stop` is **not included**.
- `s[:3]` gives the first 3 characters, `s[3:]` gives everything from index 3 on, and `s[::-1]` gives the string **reversed**.

## Immutability
`s[0] = 'J'` raises an error. Build a new string instead: `'J' + s[1:]`.

## Examples

### Example 1: Indexing  ([`example_1.py`](example_1.py))

```python
s = "Python"
print(s[0], s[1], s[-1], s[-2])
print("Length:", len(s))
print("Last char using len:", s[len(s) - 1])
```

### Example 2: Slicing  ([`example_2.py`](example_2.py))

```python
s = "Programming"
print(s[0:3])      # Pro
print(s[3:])       # gramming
print(s[:-3])      # Programm
print(s[::2])      # every 2nd character
print(s[::-1])     # reversed
```

### Example 3: Strings are immutable and can be joined  ([`example_3.py`](example_3.py))

```python
s = "hello"
# s[0] = "H"  -> TypeError
s = "H" + s[1:]
print(s)
print("ha" * 3)
word = "level"
print(word, "is a palindrome?", word == word[::-1])
multi = """This string
spans multiple
lines"""
print(multi)
```

## Practice

1. From `"NIT Kurukshetra"`, slice out `"Kurukshetra"`.
2. Print the middle character of a string with an odd length.
3. Check whether an entered word is a palindrome.

---

[⬅ Day 008](../Day-008-Operators/README.md) · [🏠 Home](../README.md) · [Day 010 ➡](../Day-010-String-Methods/README.md)
