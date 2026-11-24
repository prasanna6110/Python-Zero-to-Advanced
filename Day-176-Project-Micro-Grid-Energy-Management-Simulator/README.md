# Day 176 · Project: Micro-Grid Energy Management Simulator

_Projects_

**Concepts:** time-step simulation, classes for physical components (solar PV, a battery with a state of charge, a load, the grid), an energy-dispatch strategy, time-of-use pricing, cost and CO₂ reports.

A **micro-grid** combines local generation (solar), storage (a battery) and loads, and can import from or export to the main grid. This project simulates 24 hours and compares strategies, so it's directly connected to power systems engineering!

## Code

### Micro-Grid Simulator  ([`main.py`](main.py))

```python
import math
import random
from dataclasses import dataclass

random.seed(13)

@dataclass
class SolarPV:
    capacity_kw: float
    def output(self, hour, cloudiness):
        if not 6 <= hour <= 18:
            return 0.0
        return self.capacity_kw * math.sin(math.pi * (hour - 6) / 12) * (1 - cloudiness)

@dataclass
class Battery:
    capacity_kwh: float
    max_power_kw: float
    efficiency: float = 0.95
    soc: float = 0.5                               # state of charge (0..1)
    def charge(self, kw):
        room = (1 - self.soc) * self.capacity_kwh / self.efficiency
        p = min(kw, self.max_power_kw, room)
        self.soc += p * self.efficiency / self.capacity_kwh
        return p
    def discharge(self, kw):
        available = (self.soc - 0.1) * self.capacity_kwh * self.efficiency     # keep 10% reserve
        p = max(0.0, min(kw, self.max_power_kw, available))
        self.soc -= p / self.efficiency / self.capacity_kwh
        return p

def load_profile(hour):
    base = 8 + 4 * math.exp(-((hour - 9) ** 2) / 4) + 9 * math.exp(-((hour - 20) ** 2) / 5)   # morning and evening peaks
    return base * random.uniform(0.93, 1.07)

def tariff(hour):
    return 9.5 if 18 <= hour < 22 else 4.0 if hour < 6 else 6.5       # ₹/kWh: peak, off-peak, normal

def simulate(strategy, battery_kwh=40, pv_kw=25):
    random.seed(13)
    pv, bat = SolarPV(pv_kw), Battery(battery_kwh, 10)
    totals = {"cost": 0.0, "import": 0.0, "export": 0.0, "solar": 0.0, "load": 0.0}
    rows = []
    for hour in range(24):
        cloud = random.uniform(0, 0.4)
        gen, load = pv.output(hour, cloud), load_profile(hour)
        net = gen - load
        bat_flow = 0.0
        if strategy == "no battery":
            pass
        elif net > 0:
            bat_flow = bat.charge(net)                                       # store the surplus solar
        elif strategy == "self-consumption" or tariff(hour) > 4:   # smart: never discharge in cheap night hours
            bat_flow = -bat.discharge(-net)                                  # cover the deficit
        if strategy == "smart" and hour < 6 and bat.soc < 0.6:
            bat_flow += bat.charge(3)                                        # charge cheaply at night
        grid = load + bat_flow - gen                                         # + import / - export
        price = tariff(hour)
        totals["cost"] += grid * price if grid > 0 else grid * 3.0          # export pays ₹3/kWh
        totals["import"] += max(grid, 0); totals["export"] += max(-grid, 0)
        totals["solar"] += gen; totals["load"] += load
        rows.append((hour, gen, load, bat_flow, bat.soc, grid, price))
    return totals, rows

if __name__ == "__main__":
    _, rows = simulate("smart")
    print("⚡ 24-hour micro-grid simulation (smart strategy)")
    print(f"{'Hr':>2} {'PV kW':>6} {'Load':>6} {'Batt':>6} {'SoC':>5} {'Grid':>6} {'₹/kWh':>6}")
    for h, g, l, b, soc, grid, price in rows:
        bar = "█" * int(soc * 10)
        print(f"{h:>2} {g:>6.1f} {l:>6.1f} {b:>+6.1f} {soc:>5.0%} {grid:>+6.1f} {price:>6.1f}  {bar}")
    print(f"\n{'Strategy':<18}{'Cost ₹':>9}{'Import kWh':>12}{'Export kWh':>12}{'Self-sufficiency':>18}{'CO₂ kg':>8}")
    for s in ["no battery", "self-consumption", "smart"]:
        t, _ = simulate(s)
        self_suff = 1 - t["import"] / t["load"]
        print(f"{s:<18}{t['cost']:>9.0f}{t['import']:>12.1f}{t['export']:>12.1f}{self_suff:>18.0%}{t['import'] * 0.82:>8.1f}")
    print("\n(Grid emission factor: 0.82 kg CO₂/kWh. Battery: 40 kWh / 10 kW. PV: 25 kWp.)")
```

## Extend this project

1. Add a diesel generator for island mode when the grid fails.
2. Optimise the battery size: run the simulation for 10 to 100 kWh and find the best cost-to-size ratio.
3. Use real solar irradiance data (NASA POWER API) for Kurukshetra.

---

[⬅ Day 175](../Day-175-Project-Stock-Portfolio-Simulator/README.md) · [🏠 Home](../README.md)
