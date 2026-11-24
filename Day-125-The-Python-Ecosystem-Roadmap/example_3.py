# Day 125 · The Python Ecosystem Roadmap — A tiny neural network from scratch (the core idea behind deep learning)
# Run: python example_3.py

import math, random

random.seed(42)
# Learn XOR with a 2-4-1 network using only the standard library
X = [(0, 0), (0, 1), (1, 0), (1, 1)]
Y = [0, 1, 1, 0]
H = 4
w1 = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(H)]
b1 = [0.0] * H
w2 = [random.uniform(-1, 1) for _ in range(H)]
b2 = 0.0
sig = lambda z: 1 / (1 + math.exp(-z))
lr = 0.5

for epoch in range(10_000):
    loss = 0
    for (x1, x2), y in zip(X, Y):
        h = [sig(w1[j][0] * x1 + w1[j][1] * x2 + b1[j]) for j in range(H)]
        out = sig(sum(w2[j] * h[j] for j in range(H)) + b2)
        loss += (out - y) ** 2
        d_out = (out - y) * out * (1 - out)                 # backpropagation
        for j in range(H):
            d_h = d_out * w2[j] * h[j] * (1 - h[j])
            w2[j] -= lr * d_out * h[j]
            w1[j][0] -= lr * d_h * x1
            w1[j][1] -= lr * d_h * x2
            b1[j] -= lr * d_h
        b2 -= lr * d_out
    if epoch % 2500 == 0:
        print(f"epoch {epoch:>5} loss {loss:.4f}")

for (x1, x2), y in zip(X, Y):
    h = [sig(w1[j][0] * x1 + w1[j][1] * x2 + b1[j]) for j in range(H)]
    out = sig(sum(w2[j] * h[j] for j in range(H)) + b2)
    print(f"XOR({x1},{x2}) = {out:.3f} (target {y})")
print("Next step: build the same network in PyTorch in about 10 lines!")
