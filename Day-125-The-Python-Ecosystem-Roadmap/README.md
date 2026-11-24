# Day 125 · The Python Ecosystem Roadmap

_Ultra Advanced_

## Where to go after this course
| Field | Libraries to learn |
|-------|--------------------|
| **Data Science** | NumPy, pandas, Polars, Matplotlib, Seaborn, Plotly, Jupyter |
| **Machine Learning** | scikit-learn, XGBoost, LightGBM |
| **Deep Learning / AI** | PyTorch, TensorFlow/Keras, JAX, Hugging Face Transformers, LangChain/LlamaIndex |
| **Web Backend** | FastAPI, Django, Flask, SQLAlchemy, Pydantic, Celery |
| **Automation / Scraping** | requests, httpx, BeautifulSoup, Selenium, Playwright, Scrapy |
| **Scientific / Engineering** | SciPy, SymPy, pandapower, control, SimPy |
| **CLI / Tools** | Typer, Click, Rich, Textual |
| **GUI** | Tkinter, PyQt/PySide, Kivy, Flet |
| **Testing / Quality** | pytest, hypothesis, mypy, ruff, black, pre-commit |
| **Performance** | Cython, Numba, PyPy, Rust + PyO3 |
| **DevOps** | Docker, Ansible, boto3 (AWS), FastAPI + uvicorn |

## The habits that matter
Use Git and GitHub every day, read other people's code, write tests, build **real projects**, and contribute to open source.

> The examples below run even if these libraries aren't installed. They'll show you how to install them.

## Examples

### Example 1: NumPy-style vectorisation (with a pure-Python fallback)  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: pandas-style data analysis (with a standard-library fallback)  ([`example_2.py`](example_2.py))

```python
import csv, io, statistics
from collections import defaultdict

CSV = """name,dept,salary
Asha,EE,52000
Ravi,CS,61000
Meera,EE,58000
Kiran,CS,72000
Zoya,ME,49000
"""
try:
    import pandas as pd
    df = pd.read_csv(io.StringIO(CSV))
    print(df.groupby("dept")["salary"].agg(["mean", "max", "count"]))
except ImportError:
    print("pandas not installed -> pip install pandas. Using the standard library instead:")
    groups = defaultdict(list)
    for row in csv.DictReader(io.StringIO(CSV)):
        groups[row["dept"]].append(int(row["salary"]))
    print(f"{'dept':<5}{'mean':>10}{'max':>8}{'count':>7}")
    for dept, s in sorted(groups.items()):
        print(f"{dept:<5}{statistics.mean(s):>10.1f}{max(s):>8}{len(s):>7}")
```

### Example 3: A tiny neural network from scratch (the core idea behind deep learning)  ([`example_3.py`](example_3.py))

```python
import math, random

random.seed(42)
# Learn XOR with a 2-4-1 network using only the standard library
X = [(0, 0), (0, 1), (1, 0), (1, 1)]
Y = [0, 1, 1, 0]
H = 4
w1 = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(H)]
b1 = [0.0] * H
w2 = [random.uniform(-1, 1) for _ in range(H)]
b2 = 0.0
sig = lambda z: 1 / (1 + math.exp(-z))
lr = 0.5

for epoch in range(10_000):
    loss = 0
    for (x1, x2), y in zip(X, Y):
        h = [sig(w1[j][0] * x1 + w1[j][1] * x2 + b1[j]) for j in range(H)]
        out = sig(sum(w2[j] * h[j] for j in range(H)) + b2)
        loss += (out - y) ** 2
        d_out = (out - y) * out * (1 - out)                 # backpropagation
        for j in range(H):
            d_h = d_out * w2[j] * h[j] * (1 - h[j])
            w2[j] -= lr * d_out * h[j]
            w1[j][0] -= lr * d_h * x1
            w1[j][1] -= lr * d_h * x2
            b1[j] -= lr * d_h
        b2 -= lr * d_out
    if epoch % 2500 == 0:
        print(f"epoch {epoch:>5} loss {loss:.4f}")

for (x1, x2), y in zip(X, Y):
    h = [sig(w1[j][0] * x1 + w1[j][1] * x2 + b1[j]) for j in range(H)]
    out = sig(sum(w2[j] * h[j] for j in range(H)) + b2)
    print(f"XOR({x1},{x2}) = {out:.3f} (target {y})")
print("Next step: build the same network in PyTorch in about 10 lines!")
```

## Practice

1. Pick ONE field from the table and build a project with its main library.
2. Rebuild the XOR network in PyTorch.
3. Build a FastAPI version of the HTTP server from the networking topic.

---

[⬅ Day 124](../Day-124-Software-Architecture-Plugins-Dependency-Injection-and-Clean-Code/README.md) · [🏠 Home](../README.md) · [Day 126 ➡](../Day-126-Writing-Pythonic-Code-Idioms-and-Best-Practices/README.md)
