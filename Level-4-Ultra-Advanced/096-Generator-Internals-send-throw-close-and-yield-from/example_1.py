# 096 · Generator Internals: send, throw, close and yield from — Example 1: send(): a running-average coroutine
# Run: python example_1.py

import inspect

def averager():
    total = count = 0
    average = None
    while True:
        value = yield average          # receives a value, sends back the average
        total += value
        count += 1
        average = total / count

avg = averager()
print(inspect.getgeneratorstate(avg))
next(avg)                              # prime it
print(inspect.getgeneratorstate(avg))
for v in [10, 20, 30, 100]:
    print(f"sent {v:>3} -> average {avg.send(v):.2f}")
avg.close()
print(inspect.getgeneratorstate(avg))
