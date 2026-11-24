# Day 019 · Function Arguments in Depth — Positional-only, keyword-only and the mutable default bug
# Run: python example_3.py

def power(base, exp, /, *, verbose=False):
    result = base ** exp
    if verbose:
        print(f"{base}^{exp} = {result}")
    return result

power(2, 5, verbose=True)
# power(base=2, exp=5) -> TypeError (positional-only)

def bad_append(x, items=[]):
    items.append(x)
    return items

def good_append(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

print(bad_append(1), bad_append(2))    # shared list!
print(good_append(1), good_append(2))
