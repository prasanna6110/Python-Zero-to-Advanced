# 067 · Debugging Techniques — Example 3: Driving pdb from a script
# Run: python example_3.py

import pdb, io, sys

def buggy_sum(n):
    total = 0
    for i in range(n):     # bug: should be range(n + 1)
        total += i
    return total

# Normally you would put breakpoint() inside buggy_sum and type commands yourself.
# Here we feed pdb commands automatically to show what a session looks like.
commands = io.StringIO("p n\nn\nn\np total\nc\n")
debugger = pdb.Pdb(stdin=commands, stdout=sys.stdout)
debugger.use_rawinput = False
result = debugger.runcall(buggy_sum, 5)
print("\nResult:", result, "(expected 15 -> found the bug!)")
