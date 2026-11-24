# 016 · Function Arguments in Depth — Example 1: Default and keyword arguments
# Run: python example_1.py

def make_coffee(size="medium", sugar=1, milk=True):
    return f"{size} coffee, {sugar} sugar, {'with' if milk else 'no'} milk"

print(make_coffee())
print(make_coffee("large"))
print(make_coffee(sugar=0, milk=False))
