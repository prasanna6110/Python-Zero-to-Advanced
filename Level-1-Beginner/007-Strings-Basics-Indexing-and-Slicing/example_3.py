# 007 · Strings Basics: Indexing and Slicing — Example 3: Strings are immutable and can be joined
# Run: python example_3.py

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
