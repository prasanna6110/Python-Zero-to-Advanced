# 062 · itertools — Example 2: Combinatorics
# Run: python example_2.py

from itertools import product, permutations, combinations

print(list(product("AB", [1, 2])))
print(list(permutations("ABC", 2)))
print(list(combinations([1, 2, 3, 4], 2)))
pins = ["".join(p) for p in product("01", repeat=3)]
print("All 3-bit strings:", pins)
team = ["Asha", "Ravi", "Meera", "Kiran"]
print("Pairs for a project:", len(list(combinations(team, 2))))
