# Day 091 · Python Internals: Bytecode and dis — Why local variables are faster
# Run: python example_3.py

import dis, timeit, math

def use_global(n):
    return [math.sqrt(i) for i in range(n)]

def use_local(n):
    sqrt = math.sqrt                    # look up once, keep it in a local
    return [sqrt(i) for i in range(n)]

print("global:", timeit.timeit(lambda: use_global(10_000), number=200))
print("local :", timeit.timeit(lambda: use_local(10_000), number=200))
ops = {ins.opname for ins in dis.get_instructions(use_global)}
print("some opcodes used:", sorted(ops)[:8])
