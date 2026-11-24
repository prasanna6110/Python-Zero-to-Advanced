# Day 075 · pytest and doctest — pytest-style tests (works with or without pytest installed)
# Run: python example_2.py

# Save as test_cart.py and run:  pytest -v
try:
    import pytest
except ImportError:
    pytest = None

def cart_total(prices, discount=0):
    if not 0 <= discount <= 100:
        raise ValueError("bad discount")
    return round(sum(prices) * (1 - discount / 100), 2)

def test_total():
    assert cart_total([100, 200]) == 300

def test_discount():
    assert cart_total([100], discount=10) == 90

def test_bad_discount():
    try:
        cart_total([1], discount=200)
        assert False, "expected ValueError"
    except ValueError:
        pass

if __name__ == "__main__":
    for t in [test_total, test_discount, test_bad_discount]:
        t()
        print("PASSED", t.__name__)
    print("pytest installed:", pytest is not None)
