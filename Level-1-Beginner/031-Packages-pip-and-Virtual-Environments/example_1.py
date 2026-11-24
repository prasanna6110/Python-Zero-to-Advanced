# 031 · Packages, pip and Virtual Environments — Example 1: Building a package on the fly
# Run: python example_1.py

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
