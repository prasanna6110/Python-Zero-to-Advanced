# Day 109 · Generator Internals: send, throw, close and yield from — throw() and close() for control and cleanup
# Run: python example_2.py

class ResetSignal(Exception):
    pass

def counter():
    n = 0
    try:
        while True:
            try:
                yield n
                n += 1
            except ResetSignal:
                print("  -> reset received")
                n = 0
    finally:
        print("  -> generator closed, releasing resources")

c = counter()
print(next(c), next(c), next(c))
print("after throw:", c.throw(ResetSignal))
print(next(c))
c.close()
