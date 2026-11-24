# Day 134 · Project: Dice Rolling Simulator and Probability Lab — Dice Simulator
# Run: python main.py

import random
import sys
from collections import Counter
from itertools import product

DEMO = not sys.stdin.isatty()
FACES = {
    1: ["┌───────┐", "│       │", "│   ●   │", "│       │", "└───────┘"],
    2: ["┌───────┐", "│ ●     │", "│       │", "│     ● │", "└───────┘"],
    3: ["┌───────┐", "│ ●     │", "│   ●   │", "│     ● │", "└───────┘"],
    4: ["┌───────┐", "│ ●   ● │", "│       │", "│ ●   ● │", "└───────┘"],
    5: ["┌───────┐", "│ ●   ● │", "│   ●   │", "│ ●   ● │", "└───────┘"],
    6: ["┌───────┐", "│ ●   ● │", "│ ●   ● │", "│ ●   ● │", "└───────┘"],
}

def show(rolls):
    for line in range(5):
        print("  ".join(FACES[r][line] for r in rolls))

def experiment(n_dice=2, trials=20_000):
    sums = Counter(sum(random.randint(1, 6) for _ in range(n_dice)) for _ in range(trials))
    theory = Counter(sum(c) for c in product(range(1, 7), repeat=n_dice))
    total = 6 ** n_dice
    print(f"\n{'Sum':>4} {'Simulated':>10} {'Theory':>8}")
    for s in sorted(theory):
        sim = sums[s] / trials
        print(f"{s:>4} {sim:>10.3%} {theory[s] / total:>8.3%}  {'█' * int(sim * 150)}")

def main():
    print("🎲 DICE SIMULATOR")
    rounds = 2 if DEMO else 100
    for _ in range(rounds):
        n = 3 if DEMO else int(input("How many dice? ") or 2)
        rolls = [random.randint(1, 6) for _ in range(n)]
        show(rolls)
        print("Total:", sum(rolls))
        if not DEMO and input("Roll again? (y/n) ").lower() != "y":
            break
    experiment()

if __name__ == "__main__":
    if DEMO:
        random.seed(1)
    main()
