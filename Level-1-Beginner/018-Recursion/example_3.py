# 018 · Recursion — Example 3: Recursion on nested data
# Run: python example_3.py

def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def hanoi(n, src="A", dst="C", via="B"):
    if n == 0:
        return
    hanoi(n - 1, src, via, dst)
    print(f"Move disk {n} {src} -> {dst}")
    hanoi(n - 1, via, dst, src)

print(flatten([1, [2, [3, [4, 5]], 6], 7]))
hanoi(3)
