# 081 · Python Internals: Bytecode and dis — Example 1: Disassembling a function
# Run: python example_1.py

import dis

def add(a, b):
    c = a + b
    return c * 2

dis.dis(add)
code = add.__code__
print("varnames:", code.co_varnames, "| consts:", code.co_consts, "| argcount:", code.co_argcount)
