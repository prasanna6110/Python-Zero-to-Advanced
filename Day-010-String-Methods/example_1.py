# Day 010 · String Methods — Case and cleaning
# Run: python example_1.py

text = "   hello PYTHON world   "
print(repr(text.strip()))
print(text.strip().title())
print(text.upper())
print(text.lower().strip().capitalize())
print("Python".swapcase())
