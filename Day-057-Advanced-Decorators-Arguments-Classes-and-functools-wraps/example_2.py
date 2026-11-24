# Day 057 · Advanced Decorators: Arguments, Classes and functools.wraps — A class-based decorator with state
# Run: python example_2.py

import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

@CountCalls
def say(msg):
    return msg

say("a"); say("b"); say("c")
print(say.__name__, "was called", say.calls, "times")
