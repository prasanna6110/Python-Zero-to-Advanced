# 061 · collections Module — Example 3: namedtuple, OrderedDict and ChainMap
# Run: python example_3.py

from collections import namedtuple, OrderedDict, ChainMap

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p, p.x, p[1], p._asdict(), p._replace(x=10))

cache = OrderedDict()
for key in ["a", "b", "c"]:
    cache[key] = key.upper()
cache.move_to_end("a")                 # mark as recently used
cache.popitem(last=False)              # evict the oldest
print(cache)

defaults = {"theme": "light", "lang": "en"}
user = {"theme": "dark"}
settings = ChainMap(user, defaults)
print(settings["theme"], settings["lang"])
