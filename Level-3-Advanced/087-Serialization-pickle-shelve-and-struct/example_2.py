# 087 · Serialization: pickle, shelve and struct — Example 2: __getstate__/__setstate__ and shelve
# Run: python example_2.py

import pickle, shelve, glob, os

class Connection:
    def __init__(self, host):
        self.host = host
        self.socket = object()          # can't be pickled meaningfully
    def __getstate__(self):
        state = self.__dict__.copy()
        del state["socket"]
        return state
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.socket = "reconnected"

c = pickle.loads(pickle.dumps(Connection("db.local")))
print(c.host, c.socket)

with shelve.open("mydb") as db:
    db["users"] = ["asha", "ravi"]
    db["config"] = {"theme": "dark"}
with shelve.open("mydb") as db:
    print(dict(db))
for f in glob.glob("mydb*"):
    os.remove(f)
