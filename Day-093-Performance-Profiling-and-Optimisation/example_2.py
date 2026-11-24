# Day 093 · Performance: Profiling and Optimisation — cProfile to find the bottleneck
# Run: python example_2.py

import cProfile, pstats, io

def slow_unique(items):
    result = []
    for x in items:
        if x not in result:         # O(n) check -> O(n²) overall
            result.append(x)
    return result

def fast_unique(items):
    return list(dict.fromkeys(items))

def main():
    data = list(range(3000)) * 2
    slow_unique(data)
    fast_unique(data)

pr = cProfile.Profile()
pr.enable(); main(); pr.disable()
out = io.StringIO()
pstats.Stats(pr, stream=out).sort_stats("cumulative").print_stats(5)
print("\n".join(out.getvalue().splitlines()[:18]))
