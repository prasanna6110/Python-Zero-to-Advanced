# Day 075 · pytest and doctest — doctest
# Run: python example_1.py

def factorial(n):
    """Return n!.

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: n must be >= 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    return 1 if n == 0 else n * factorial(n - 1)

if __name__ == "__main__":
    import doctest
    results = doctest.testmod(verbose=False)
    print(results)
