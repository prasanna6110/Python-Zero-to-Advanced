# 095 · Algorithms: Graphs, Recursion Patterns and Dynamic Programming — Example 3: Dynamic programming classics
# Run: python example_3.py

from functools import cache

def coin_change(coins, amount):
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

def knapsack(items, capacity):          # items: (weight, value)
    dp = [0] * (capacity + 1)
    for w, v in items:
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]

def lcs(a, b):
    @cache
    def go(i, j):
        if i == len(a) or j == len(b): return ""
        if a[i] == b[j]: return a[i] + go(i + 1, j + 1)
        return max(go(i + 1, j), go(i, j + 1), key=len)
    return go(0, 0)

def edit_distance(s, t):
    dp = list(range(len(t) + 1))
    for i in range(1, len(s) + 1):
        prev, dp[0] = dp[0], i
        for j in range(1, len(t) + 1):
            prev, dp[j] = dp[j], min(dp[j] + 1, dp[j - 1] + 1, prev + (s[i - 1] != t[j - 1]))
    return dp[-1]

print("coins for ₹11 with [1,2,5]:", coin_change([1, 2, 5], 11))
print("knapsack:", knapsack([(1, 1), (3, 4), (4, 5), (5, 7)], 7))
print("LCS:", lcs("AGGTAB", "GXTXAYB"))
print("edit distance kitten->sitting:", edit_distance("kitten", "sitting"))
