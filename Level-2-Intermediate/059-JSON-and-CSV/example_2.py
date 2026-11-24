# 059 · JSON and CSV — Example 2: Serialising custom objects
# Run: python example_2.py

import json
from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class Event:
    title: str
    day: date

def encoder(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Can't serialise {type(obj)}")

events = [Event("Mid-term", date(2026, 11, 28)), Event("Project demo", date(2026, 12, 5))]
payload = json.dumps([asdict(e) for e in events], default=encoder, indent=1)
print(payload)
loaded = [Event(d["title"], date.fromisoformat(d["day"])) for d in json.loads(payload)]
print(loaded[0])
