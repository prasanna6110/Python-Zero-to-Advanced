# 112 · The Python Ecosystem Roadmap — Example 1: NumPy-style vectorisation (with a pure-Python fallback)
# Run: python example_1.py

import time

try:
    import numpy as np
    a = np.arange(1_000_000, dtype=np.float64)
    start = time.perf_counter()
    result = (a ** 2 + 3 * a).sum()
    print(f"NumPy vectorised: {result:.3e} in {time.perf_counter() - start:.4f}s")
except ImportError:
    print("NumPy not installed -> pip install numpy")

start = time.perf_counter()
result = sum(x * x + 3 * x for x in range(1_000_000))
print(f"Pure Python loop: {result:.3e} in {time.perf_counter() - start:.4f}s")
