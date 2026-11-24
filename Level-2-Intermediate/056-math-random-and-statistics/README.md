# 056 · math, random and statistics

## math
`sqrt, pow, floor, ceil, trunc, factorial, gcd, lcm, comb, perm, log, log10, log2, exp, sin, cos, radians, degrees, pi, e, inf, isclose, prod, hypot, dist`

## random (pseudo-random; **not** secure. Use `secrets` for passwords)
| Function | Use |
|----------|-----|
| `random()` | a float from 0 to 1 |
| `randint(a, b)` | an int from a to b, inclusive |
| `uniform(a, b)` | a float between a and b |
| `choice(seq)`, `choices(seq, k=, weights=)` | pick one / pick many with replacement |
| `sample(seq, k)` | pick many without replacement |
| `shuffle(lst)` | shuffle in place |
| `seed(n)` | makes the results reproducible |

## statistics
`mean, median, mode, stdev, variance, quantiles`

## Examples

### Example 1: math functions  ([`example_1.py`](example_1.py))

```python
import math

print(math.sqrt(144), math.floor(3.7), math.ceil(3.2), math.trunc(-3.7))
print(math.factorial(6), math.gcd(48, 36), math.lcm(4, 6))
print(math.comb(5, 2), math.perm(5, 2))         # nCr, nPr
print(math.log(100, 10), math.log2(1024), math.exp(1))
print(math.sin(math.radians(30)), math.hypot(3, 4))
print(0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))
```

### Example 2: random module  ([`example_2.py`](example_2.py))

```python
import random

random.seed(42)          # reproducible results
print(random.randint(1, 6), random.random(), random.uniform(1, 10))
colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors))
print(random.sample(colors, 2))
print(random.choices(["win", "lose"], weights=[1, 9], k=10))
deck = list(range(1, 11))
random.shuffle(deck)
print(deck)
```

### Example 3: Simulation with statistics: dice rolls  ([`example_3.py`](example_3.py))

```python
import random, statistics
from collections import Counter

random.seed(7)
rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10_000)]
counts = Counter(rolls)
for total in range(2, 13):
    bar = "#" * (counts[total] // 50)
    print(f"{total:>2}: {bar}")
print("mean:", round(statistics.mean(rolls), 3), "mode:", statistics.mode(rolls),
      "stdev:", round(statistics.stdev(rolls), 3))
```

## Practice

1. Write an OTP generator (then redo it properly with `secrets`).
2. Estimate π with a Monte Carlo simulation.
3. Find the median and standard deviation of your semester marks.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
