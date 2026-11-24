# 086 · Functional Programming in Python — Example 3: Currying and the operator module
# Run: python example_3.py

from functools import partial, reduce
import operator

def curry(f, n):
    def curried(*args):
        if len(args) >= n:
            return f(*args)
        return lambda *more: curried(*args, *more)
    return curried

volume = curry(lambda l, w, h: l * w * h, 3)
print(volume(2)(3)(4), volume(2, 3)(4), volume(2, 3, 4))

orders = [{"item": "pen", "qty": 3, "price": 10}, {"item": "book", "qty": 2, "price": 250}]
get_cost = lambda o: operator.mul(o["qty"], o["price"])
print(reduce(operator.add, map(get_cost, orders)))
print(list(map(partial(operator.mul, 3), [1, 2, 3])))
print(sorted(orders, key=operator.itemgetter("price"), reverse=True)[0]["item"])
