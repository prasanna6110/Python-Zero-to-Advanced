# 031 · Packages, pip and Virtual Environments

## Packages
A **package** is a folder of modules. It usually has an `__init__.py` file.
```
shop/
    __init__.py
    cart.py
    payment/
        __init__.py
        upi.py
```
`from shop.payment.upi import pay`

## pip: the package installer
```bash
pip install requests
pip install requests==2.32.0
pip uninstall requests
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```
## Virtual environments: an isolated set of packages per project
```bash
python -m venv .venv
# Windows:      .venv\Scripts\activate
# Mac / Linux:  source .venv/bin/activate
deactivate
```
Always use a venv for each project so their package versions never clash.

## Examples

### Example 1: Building a package on the fly  ([`example_1.py`](example_1.py))

```python
import pathlib, sys, shutil

root = pathlib.Path("shop")
(root / "payment").mkdir(parents=True, exist_ok=True)
(root / "__init__.py").write_text('VERSION = "1.0"\n')
(root / "cart.py").write_text("def total(items):\n    return sum(items)\n")
(root / "payment" / "__init__.py").write_text("")
(root / "payment" / "upi.py").write_text("def pay(amount):\n    return f'Paid ₹{amount} via UPI'\n")

sys.path.insert(0, ".")
import shop
from shop.cart import total
from shop.payment.upi import pay
print(shop.VERSION, pay(total([100, 250])))
shutil.rmtree(root)
```

### Example 2: Checking installed packages from code  ([`example_2.py`](example_2.py))

```python
from importlib import metadata

for pkg in ["pip", "setuptools", "requests"]:
    try:
        print(f"{pkg}: {metadata.version(pkg)}")
    except metadata.PackageNotFoundError:
        print(f"{pkg}: not installed  (run: pip install {pkg})")
```

### Example 3: Are we inside a virtual environment?  ([`example_3.py`](example_3.py))

```python
import sys

in_venv = sys.prefix != sys.base_prefix
print("Inside virtual env:", in_venv)
print("sys.prefix:", sys.prefix)
print("Tip: create one with  python -m venv .venv")
```

## Practice

1. Create a venv, install `requests` in it and write a `requirements.txt`.
2. Build a `utils` package with `math_utils` and `string_utils` modules.
3. What is the job of `__init__.py`?

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
