# 087 · Serialization: pickle, shelve and struct — Example 1: pickle round trip
# Run: python example_1.py

import pickle
from datetime import datetime

class Session:
    def __init__(self, user):
        self.user = user
        self.started = datetime(2026, 11, 24, 10, 0)
        self.cart = {"laptop": 1}

s = Session("prasanna")
data = pickle.dumps(s)
print(type(data), len(data), "bytes")
restored = pickle.loads(data)
print(restored.user, restored.started, restored.cart)

with open("session.pkl", "wb") as f:
    pickle.dump([s, {1, 2, 3}, (4, 5)], f)
with open("session.pkl", "rb") as f:
    print(pickle.load(f)[1:])
import os; os.remove("session.pkl")
