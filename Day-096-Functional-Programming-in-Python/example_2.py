# Day 096 · Functional Programming in Python — Composition and pipelines
# Run: python example_2.py

from functools import reduce

def compose(*funcs):
    return lambda x: reduce(lambda acc, f: f(acc), reversed(funcs), x)

def pipe(*funcs):
    return lambda x: reduce(lambda acc, f: f(acc), funcs, x)

strip = str.strip
lower = str.lower
words = str.split
unique_sorted = lambda ws: sorted(set(ws))

clean = pipe(strip, lower, words, unique_sorted)
print(clean("   The quick brown fox jumps over THE lazy dog   "))
inc = lambda x: x + 1
dbl = lambda x: x * 2
print(compose(inc, dbl)(5), pipe(inc, dbl)(5))   # inc(dbl(5)) vs dbl(inc(5))
