# Day 174 · Project: K-Means Clustering from Scratch (Customer Segmentation)

_Projects_

**Concepts:** unsupervised learning, Euclidean distance, centroid updates, convergence, k-means++ initialisation, the **elbow method** for choosing k.

It groups shop customers by annual income and spending score into segments like "premium" and "budget", with no labels needed.

## Code

### K-Means Customer Segmentation  ([`main.py`](main.py))

```python
import math
import random

random.seed(5)
def blob(cx, cy, n, spread):
    return [(random.gauss(cx, spread), random.gauss(cy, spread)) for _ in range(n)]

customers = blob(25, 80, 25, 6) + blob(85, 85, 25, 7) + blob(55, 50, 30, 6) + blob(85, 15, 20, 6) + blob(25, 20, 20, 6)

def dist(a, b):
    return math.dist(a, b)

def kmeans_pp_init(points, k):
    centroids = [random.choice(points)]
    while len(centroids) < k:
        d2 = [min(dist(p, c) ** 2 for c in centroids) for p in points]
        centroids.append(random.choices(points, weights=d2)[0])     # pick points far from the existing centroids
    return centroids

def kmeans(points, k, iters=100):
    centroids = kmeans_pp_init(points, k)
    for it in range(iters):
        clusters = [[] for _ in range(k)]
        for p in points:
            clusters[min(range(k), key=lambda i: dist(p, centroids[i]))].append(p)
        new = [(sum(x for x, _ in c) / len(c), sum(y for _, y in c) / len(c)) if c else centroids[i]
               for i, c in enumerate(clusters)]
        if all(dist(a, b) < 1e-6 for a, b in zip(new, centroids)):
            break
        centroids = new
    inertia = sum(dist(p, centroids[i]) ** 2 for i, c in enumerate(clusters) for p in c)
    return centroids, clusters, inertia, it + 1

def label(c):
    income, spend = c
    if income > 70 and spend > 60: return "💎 Premium"
    if income > 70: return "🧐 Careful rich"
    if spend > 60: return "🛍 Impulsive"
    if income < 40 and spend < 40: return "🪙 Budget"
    return "🙂 Average"

def plot(clusters, width=50, height=15):
    grid = [[" "] * width for _ in range(height)]
    for i, c in enumerate(clusters):
        for x, y in c:
            grid[height - 1 - min(height - 1, int(y / 100 * height))][min(width - 1, int(x / 110 * width))] = "ABCDE"[i]
    print("spending\n" + "\n".join("|" + "".join(r) for r in grid) + "\n+" + "-" * width + " income (k₹)")

if __name__ == "__main__":
    print("Elbow method (inertia goes down as k goes up; look for the bend):")
    for k in range(1, 8):
        inertia = kmeans(customers, k)[2]
        print(f"  k={k}: {inertia:>9.0f} {'█' * int(inertia / 4000)}")
    centroids, clusters, _, iters = kmeans(customers, 5)
    print(f"\nk=5 converged in {iters} iterations")
    for i, (c, members) in enumerate(sorted(zip(centroids, clusters))):
        print(f"  {'ABCDE'[i]}: income {c[0]:5.1f}k, score {c[1]:5.1f} | {len(members):>2} customers | {label(c)}")
    plot([m for _, m in sorted(zip(centroids, clusters))])
```

## Extend this project

1. Cluster the real Mall Customers dataset from Kaggle.
2. Add the silhouette score to choose k automatically.
3. Compare your results with `sklearn.cluster.KMeans`.

---

[⬅ Day 173](../Day-173-Project-Linear-Regression-from-Scratch-Marks-Predictor/README.md) · [🏠 Home](../README.md) · [Day 175 ➡](../Day-175-Project-Stock-Portfolio-Simulator/README.md)
