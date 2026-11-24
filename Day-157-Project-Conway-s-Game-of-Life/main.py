# Day 157 · Project: Conway's Game of Life — Game of Life (sparse set implementation)
# Run: python main.py

import os
import sys
import time
from collections import Counter

DEMO = not sys.stdin.isatty()
PATTERNS = {
    "glider": {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)},
    "blinker": {(1, 0), (1, 1), (1, 2)},
    "r-pentomino": {(1, 0), (2, 0), (0, 1), (1, 1), (1, 2)},
    "gosper glider gun": {(0, 4), (0, 5), (1, 4), (1, 5), (10, 4), (10, 5), (10, 6), (11, 3), (11, 7), (12, 2),
                          (12, 8), (13, 2), (13, 8), (14, 5), (15, 3), (15, 7), (16, 4), (16, 5), (16, 6),
                          (17, 5), (20, 2), (20, 3), (20, 4), (21, 2), (21, 3), (21, 4), (22, 1), (22, 5),
                          (24, 0), (24, 1), (24, 5), (24, 6), (34, 2), (34, 3), (35, 2), (35, 3)},
}

def step(live):
    counts = Counter((x + dx, y + dy) for x, y in live
                     for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0))
    return {cell for cell, n in counts.items() if n == 3 or (n == 2 and cell in live)}

def render(live, w=40, h=14):
    return "\n".join("".join("█" if (x, y) in live else "·" for x in range(w)) for y in range(h))

def run(name, generations, delay):
    live = {(x + 1, y + 1) for x, y in PATTERNS[name]}
    for g in range(generations):
        if not DEMO:
            os.system("cls" if os.name == "nt" else "clear")
        if not DEMO or g in (0, generations - 1):
            print(f"{name} | generation {g} | population {len(live)}")
            print(render(live))
        live = step(live)
        time.sleep(delay)

if __name__ == "__main__":
    if DEMO:
        run("glider", 9, 0)
        run("gosper glider gun", 31, 0)
    else:
        print("Patterns:", ", ".join(PATTERNS))
        name = input("Choose a pattern: ").strip() or "glider"
        run(name if name in PATTERNS else "glider", 200, 0.1)
