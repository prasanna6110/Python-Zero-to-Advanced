# Day 102 · Working with Excel, PDF and Images (Popular Libraries) — Charts with matplotlib (text chart fallback)
# Run: python example_3.py

import os

months = ["Jul", "Aug", "Sep", "Oct", "Nov"]
hours = [12, 20, 26, 31, 40]
try:
    import matplotlib
    matplotlib.use("Agg")                        # save to a file without opening a window
    import matplotlib.pyplot as plt
    plt.plot(months, hours, marker="o")
    plt.title("Python practice hours"); plt.ylabel("hours")
    plt.savefig("progress.png", dpi=80)
    print("Saved progress.png")
    os.remove("progress.png")
except ImportError:
    print("matplotlib not installed (pip install matplotlib). Text chart:")
    for m, h in zip(months, hours):
        print(f"{m} {'█' * (h // 2)} {h}")
