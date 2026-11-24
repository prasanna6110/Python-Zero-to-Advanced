# Day 069 · Regular Expressions (re) — Named groups and parsing logs
# Run: python example_2.py

import re

LOG = re.compile(
    r"(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>[^\]]+)\] \"(?P<method>GET|POST) (?P<path>\S+)\" (?P<status>\d{3})"
)
lines = [
    '10.0.0.1 - [24/Nov/2026:10:00:01] "GET /index.html" 200',
    '10.0.0.2 - [24/Nov/2026:10:00:05] "POST /login" 401',
]
for line in lines:
    m = LOG.search(line)
    if m:
        d = m.groupdict()
        print(d["ip"], d["method"], d["path"], d["status"])
