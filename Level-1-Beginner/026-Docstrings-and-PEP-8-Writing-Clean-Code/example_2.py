# 026 · Docstrings and PEP 8 (Writing Clean Code) — Example 2: Bad style vs PEP 8 style
# Run: python example_2.py

# Bad:
def CalcTotal(L):
  t=0
  for i in L:t+=i
  return t

# Good (PEP 8):
TAX_RATE = 0.18


def calculate_total(prices):
    """Return the total of prices including tax."""
    subtotal = sum(prices)
    return subtotal * (1 + TAX_RATE)


print(CalcTotal([1, 2]), calculate_total([100, 200]))
