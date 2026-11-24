# Day 173 · Project: Linear Regression from Scratch (Marks Predictor) — Linear Regression (two ways)
# Run: python main.py

import random
import statistics

random.seed(1)
hours = [round(random.uniform(1, 10), 1) for _ in range(30)]
marks = [round(min(100, 8.2 * h + 15 + random.gauss(0, 6)), 1) for h in hours]

def closed_form(x, y):
    mx, my = statistics.mean(x), statistics.mean(y)
    slope = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return slope, my - slope * mx

def gradient_descent(x, y, lr=0.01, epochs=3000):
    w = b = 0.0
    n = len(x)
    for epoch in range(epochs):
        preds = [w * a + b for a in x]
        dw = (2 / n) * sum((p - t) * a for p, t, a in zip(preds, y, x))
        db = (2 / n) * sum(p - t for p, t in zip(preds, y))
        w -= lr * dw
        b -= lr * db
        if epoch % 1000 == 0:
            mse = sum((p - t) ** 2 for p, t in zip(preds, y)) / n
            print(f"  epoch {epoch:>4}: w={w:6.3f} b={b:6.3f} MSE={mse:8.2f}")
    return w, b

def r2(x, y, w, b):
    my = statistics.mean(y)
    ss_res = sum((t - (w * a + b)) ** 2 for a, t in zip(x, y))
    ss_tot = sum((t - my) ** 2 for t in y)
    return 1 - ss_res / ss_tot

def text_plot(x, y, w, b, width=50, height=14):
    grid = [[" "] * width for _ in range(height)]
    to_col = lambda v: int((v - 1) / 9 * (width - 1))
    to_row = lambda v: height - 1 - int(max(0, min(99, v)) / 100 * (height - 1))
    for c in range(width):
        grid[to_row(w * (1 + c / (width - 1) * 9) + b)][c] = "-"
    for a, t in zip(x, y):
        grid[to_row(t)][to_col(a)] = "●"
    print("marks\n" + "\n".join("  |" + "".join(r) for r in grid) + "\n  +" + "-" * width + " hours")

if __name__ == "__main__":
    w1, b1 = closed_form(hours, marks)
    print(f"Closed form     : marks = {w1:.3f} × hours + {b1:.3f}   R² = {r2(hours, marks, w1, b1):.3f}")
    print("Gradient descent:")
    w2, b2 = gradient_descent(hours, marks)
    print(f"Gradient descent: marks = {w2:.3f} × hours + {b2:.3f}   R² = {r2(hours, marks, w2, b2):.3f}")
    text_plot(hours, marks, w1, b1)
    for h in [2, 5, 8.5]:
        print(f"📚 Study {h} h -> predicted marks ≈ {w1 * h + b1:.1f}")
