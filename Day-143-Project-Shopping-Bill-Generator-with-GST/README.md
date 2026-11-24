# Day 143 · Project: Shopping Bill Generator with GST

_Projects_

**Concepts:** dictionaries for the product catalogue, `Decimal` for money, discounts, GST slabs, formatted invoices, saving to a file.

It builds a real-looking invoice with item-wise GST (5%, 12%, 18%), coupon codes and a receipt number.

## Code

### Shopping Bill Generator  ([`main.py`](main.py))

```python
import sys
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

DEMO = not sys.stdin.isatty()
CATALOG = {
    "P01": ("Notebook (200 pages)", Decimal("60"), 12),
    "P02": ("Gel Pen pack", Decimal("120"), 18),
    "P03": ("Python book", Decimal("499"), 5),
    "P04": ("Scientific calculator", Decimal("899"), 18),
    "P05": ("Milk 1L", Decimal("66"), 5),
}
COUPONS = {"STUDENT10": Decimal("0.10"), "FEST20": Decimal("0.20")}
DEMO_INPUTS = iter(["P01 3", "P03 1", "P04 1", "P02 2", "done", "STUDENT10"])

def ask(prompt):
    if DEMO:
        v = next(DEMO_INPUTS); print(prompt + v); return v
    return input(prompt)

def money(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def main():
    print("🛒 PRODUCTS")
    for code, (name, price, gst) in CATALOG.items():
        print(f"  {code}  {name:<24} ₹{price:>7}  GST {gst}%")
    cart = {}
    while (entry := ask("Add item as 'CODE QTY' (or 'done'): ").strip()) != "done":
        try:
            code, qty = entry.split()
            if code.upper() not in CATALOG:
                raise KeyError
            cart[code.upper()] = cart.get(code.upper(), 0) + int(qty)
        except (ValueError, KeyError):
            print("  Invalid entry")
    coupon = ask("Coupon code (Enter to skip): ").strip().upper()
    discount_rate = COUPONS.get(coupon, Decimal("0"))

    lines, subtotal, gst_total = [], Decimal("0"), Decimal("0")
    for code, qty in cart.items():
        name, price, gst = CATALOG[code]
        amount = price * qty
        tax = money(amount * (1 - discount_rate) * gst / 100)
        subtotal += amount; gst_total += tax
        lines.append(f"{name:<24}{qty:>4}{price:>9}{amount:>10}{gst:>5}%{tax:>9}")
    discount = money(subtotal * discount_rate)
    grand = money(subtotal - discount + gst_total)
    now = datetime(2026, 11, 24, 18, 30) if DEMO else datetime.now()
    bill = "\n".join([
        "=" * 62, f"{'PK STATIONERY & GENERAL STORE':^62}", f"{'Kurukshetra, Haryana':^62}",
        f"Invoice #{now:%Y%m%d%H%M}      Date: {now:%d-%m-%Y %I:%M %p}", "-" * 62,
        f"{'Item':<24}{'Qty':>4}{'Rate':>9}{'Amount':>10}{'GST':>6}{'Tax':>9}", "-" * 62, *lines, "-" * 62,
        f"{'Subtotal':<50}₹{money(subtotal):>10}",
        f"{'Discount (' + (coupon or 'none') + ')':<50}-₹{discount:>9}",
        f"{'CGST + SGST':<50}₹{gst_total:>10}",
        f"{'GRAND TOTAL':<50}₹{grand:>10}", "=" * 62, f"{'Thank you! Visit again 🙏':^62}",
    ])
    print("\n" + bill)
    if not DEMO:
        with open(f"invoice_{now:%Y%m%d%H%M}.txt", "w", encoding="utf-8") as f:
            f.write(bill)

if __name__ == "__main__":
    main()
```

## Extend this project

1. Load the catalogue from a CSV file and update the stock after each sale.
2. Generate a PDF invoice with `fpdf2`.
3. Add a daily sales report.

---

[⬅ Day 142](../Day-142-Project-Number-System-Converter/README.md) · [🏠 Home](../README.md) · [Day 144 ➡](../Day-144-Project-Typing-Speed-Test/README.md)
