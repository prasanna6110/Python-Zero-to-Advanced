# 096 · Generator Internals: send, throw, close and yield from — Example 3: yield from: delegation and return values
# Run: python example_3.py

def read_chunk(name):
    total = 0
    while True:
        value = yield
        if value is None:
            return f"{name}: total={total}"    # becomes StopIteration.value
        total += value

def coordinator(results):
    while True:
        name = yield
        summary = yield from read_chunk(name)  # send() passes straight through
        results.append(summary)

results = []
co = coordinator(results)
next(co)
for group, values in {"girls": [40, 42, 39], "boys": [45, 38]}.items():
    co.send(group)
    for v in values:
        co.send(v)
    co.send(None)                              # ends the sub-generator
print(results)

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
print(list(flatten([1, [2, [3, [4]], 5]])))
