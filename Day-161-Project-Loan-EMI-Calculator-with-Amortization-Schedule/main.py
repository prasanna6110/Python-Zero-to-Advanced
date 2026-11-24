# Day 161 · Project: Loan EMI Calculator with Amortization Schedule — EMI Calculator
# Run: python main.py

import csv
import sys
from decimal import Decimal, ROUND_HALF_UP

DEMO = not sys.stdin.isatty()
D = lambda x: Decimal(str(x))
R2 = lambda x: x.quantize(D("0.01"), rounding=ROUND_HALF_UP)

def emi(principal, annual_rate, months):
    r = D(annual_rate) / 1200
    if r == 0:
        return R2(D(principal) / months)
    f = (1 + r) ** months
    return R2(D(principal) * r * f / (f - 1))

def schedule(principal, annual_rate, months, prepay=0):
    r, bal, pay = D(annual_rate) / 1200, D(principal), emi(principal, annual_rate, months)
    rows, m = [], 0
    while bal > 0:
        m += 1
        interest = R2(bal * r)
        principal_part = min(pay - interest, bal)
        bal = R2(bal - principal_part)
        extra = min(D(prepay), bal)
        bal -= extra
        rows.append((m, pay if bal > 0 else principal_part + interest, interest, principal_part + extra, bal))
    return rows

def summary(label, rows):
    total_interest = sum(r[2] for r in rows)
    print(f"{label:<28} months={len(rows):>3}  total interest=₹{total_interest:>12,.2f}")
    return total_interest

if __name__ == "__main__":
    if DEMO:
        P, rate, years = 800000, 8.5, 5
    else:
        P = float(input("Loan amount (₹): "))
        rate = float(input("Annual interest rate (%): "))
        years = float(input("Tenure (years): "))
    n = int(years * 12)
    print(f"\n🏦 Loan ₹{P:,.0f} at {rate}% for {years} years -> EMI = ₹{emi(P, rate, n):,.2f}\n")
    rows = schedule(P, rate, n)
    print(f"{'Month':>5}{'EMI':>12}{'Interest':>12}{'Principal':>12}{'Balance':>14}")
    for row in rows[:3] + rows[-2:]:
        print(f"{row[0]:>5}{row[1]:>12,.2f}{row[2]:>12,.2f}{row[3]:>12,.2f}{row[4]:>14,.2f}")
    print()
    base = summary("Normal", rows)
    for extra in (2000, 5000):
        saved = base - summary(f"With ₹{extra}/month prepay", schedule(P, rate, n, extra))
        print(f"{'':28} 💰 saves ₹{saved:,.2f}")
    if not DEMO:
        with open("amortization.csv", "w", newline="") as f:
            csv.writer(f).writerows([("month", "emi", "interest", "principal", "balance"), *rows])
        print("\nFull schedule saved to amortization.csv")
