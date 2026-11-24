# Day 127 · Common Mistakes and Gotchas — Shadowing, mutable defaults and string immutability
# Run: python example_3.py

list_backup = list
list = [1, 2, 3]                      # shadows the built-in list()
try:
    list("abc")
except TypeError as e:
    print("Shadowing bug:", e)
list = list_backup

def add_student(name, group=[]):
    group.append(name)
    return group
print(add_student("A"), add_student("B"), "<- the same list is reused!")

s = "hello"
s.upper()
print("s.upper() without assigning it:", s, "| s = s.upper():", s.upper())

import random, os
print("If you name your own file random.py, `import random` loads YOUR file.")
print("The real random module lives at:", os.path.basename(os.path.dirname(random.__file__)) + "/random.py")
