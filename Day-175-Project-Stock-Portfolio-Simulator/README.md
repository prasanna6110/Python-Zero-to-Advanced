# Day 175 · Project: Stock Portfolio Simulator

_Projects_

**Concepts:** simulating prices with a random walk (geometric Brownian motion), dataclasses, portfolio valuation, profit and loss, moving averages, a simple trading strategy and a backtest.

You get virtual money: buy and sell simulated stocks, track your profit and loss, and backtest a moving-average crossover strategy.

> Educational only. This is not financial advice, and real markets are not random walks!

## Code

### Stock Portfolio Simulator  ([`main.py`](main.py))

```python
import math
import random
from dataclasses import dataclass, field

random.seed(2026)
STOCKS = {"PYTHN": (1500, 0.12, 0.25), "GRIDX": (820, 0.08, 0.18), "SOLAR": (310, 0.15, 0.40)}   # price, drift, volatility

def simulate(price, mu, sigma, days=250):
    prices, dt = [price], 1 / 250
    for _ in range(days - 1):
        shock = random.gauss(0, 1)
        prices.append(prices[-1] * math.exp((mu - sigma ** 2 / 2) * dt + sigma * math.sqrt(dt) * shock))
    return prices

@dataclass
class Portfolio:
    cash: float = 100_000
    holdings: dict = field(default_factory=dict)       # symbol -> [qty, avg_cost]
    trades: list = field(default_factory=list)

    def buy(self, sym, qty, price, day):
        cost = qty * price
        if cost > self.cash:
            raise ValueError("not enough cash")
        q, avg = self.holdings.get(sym, [0, 0])
        self.holdings[sym] = [q + qty, (q * avg + cost) / (q + qty)]
        self.cash -= cost
        self.trades.append((day, "BUY", sym, qty, price))

    def sell(self, sym, qty, price, day):
        q, avg = self.holdings.get(sym, [0, 0])
        if qty > q:
            raise ValueError("not enough shares")
        self.holdings[sym] = [q - qty, avg]
        self.cash += qty * price
        self.trades.append((day, "SELL", sym, qty, price, (price - avg) * qty))

    def value(self, prices):
        return self.cash + sum(q * prices[s] for s, (q, _) in self.holdings.items())

def sma(series, n, i):
    return sum(series[i - n + 1:i + 1]) / n if i >= n - 1 else None

def backtest(sym, prices, fast=10, slow=30):
    pf = Portfolio()
    for i in range(len(prices)):
        f, s, pf_, ps_ = sma(prices, fast, i), sma(prices, slow, i), sma(prices, fast, i - 1), sma(prices, slow, i - 1)
        if None in (f, s, pf_, ps_):
            continue
        held = pf.holdings.get(sym, [0])[0]
        if pf_ <= ps_ and f > s and not held:                   # golden cross: buy
            pf.buy(sym, int(pf.cash // prices[i]), prices[i], i)
        elif pf_ >= ps_ and f < s and held:                     # death cross: sell
            pf.sell(sym, held, prices[i], i)
    final = pf.value({sym: prices[-1]})
    buy_hold = 100_000 / prices[0] * prices[-1]
    print(f"  {sym}: strategy ₹{final:,.0f} ({final / 1000 - 100:+.1f}%) vs buy & hold ₹{buy_hold:,.0f} "
          f"({buy_hold / 1000 - 100:+.1f}%) | {len(pf.trades)} trades")

if __name__ == "__main__":
    history = {s: simulate(*params) for s, params in STOCKS.items()}
    print("📈 One simulated year of prices:")
    for s, p in history.items():
        spark = "".join("▁▂▃▄▅▆▇█"[min(7, int((v - min(p)) / (max(p) - min(p) + 1e-9) * 8))] for v in p[::10])
        print(f"  {s}: ₹{p[0]:>7.1f} -> ₹{p[-1]:>7.1f}  {spark}")

    me = Portfolio()
    me.buy("PYTHN", 20, history["PYTHN"][0], 0)
    me.buy("SOLAR", 100, history["SOLAR"][0], 0)
    me.buy("GRIDX", 30, history["GRIDX"][100], 100)
    me.sell("SOLAR", 50, history["SOLAR"][180], 180)
    final_prices = {s: p[-1] for s, p in history.items()}
    print("\n💼 My portfolio at the end of the year:")
    for s, (q, avg) in me.holdings.items():
        pnl = (final_prices[s] - avg) * q
        print(f"  {s}: {q:>3} shares, avg ₹{avg:,.1f}, now ₹{final_prices[s]:,.1f}, P&L {'🟢' if pnl >= 0 else '🔴'} ₹{pnl:,.0f}")
    print(f"  Cash ₹{me.cash:,.0f} | Total value ₹{me.value(final_prices):,.0f} (started with ₹100,000)")
    print("\n🤖 Backtesting the moving-average crossover strategy:")
    for s, p in history.items():
        backtest(s, p)
```

## Extend this project

1. Download real historical prices (`yfinance`) and backtest on them.
2. Add brokerage fees and taxes to make it realistic.
3. Plot the prices and moving averages with matplotlib.

---

[⬅ Day 174](../Day-174-Project-K-Means-Clustering-from-Scratch-Customer-Segmentation/README.md) · [🏠 Home](../README.md) · [Day 176 ➡](../Day-176-Project-Micro-Grid-Energy-Management-Simulator/README.md)
