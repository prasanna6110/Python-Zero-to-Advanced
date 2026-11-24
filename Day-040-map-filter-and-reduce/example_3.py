# Day 040 · map, filter and reduce — reduce and a data pipeline
# Run: python example_3.py

from functools import reduce
import operator

print(reduce(operator.add, [1, 2, 3, 4]))
print(reduce(lambda a, b: a * b, range(1, 6)))       # 5!
print(reduce(lambda a, b: a if a > b else b, [3, 9, 2]))

orders = [("pen", 10, 3), ("book", 250, 1), ("bag", 900, 0)]
total = reduce(lambda acc, o: acc + o[1] * o[2],
               filter(lambda o: o[2] > 0, orders), 0)
print("Order total:", total)
