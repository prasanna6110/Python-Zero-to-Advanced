# Day 154 · Project: Log File Analyzer

_Projects_

**Concepts:** regex with named groups, `Counter`, `datetime` parsing, grouping by hour, finding anomalies, generating reports.

It parses web server access logs to find the top pages, error rates, suspicious IP addresses and the busiest hours.

## Code

### Web Server Log Analyzer  ([`main.py`](main.py))

```python
import random
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta

DEMO = not sys.stdin.isatty()
LOG_RE = re.compile(r'(?P<ip>\S+) - - \[(?P<ts>[^\]]+)\] "(?P<method>\w+) (?P<path>\S+) [^"]+" (?P<status>\d{3}) (?P<size>\d+)')

def fake_logs(n=600):
    random.seed(42)
    pages = ["/", "/courses", "/courses/python", "/login", "/api/data", "/about", "/blog/day-1"]
    ips = [f"192.168.1.{i}" for i in range(1, 20)] + ["45.33.10.99"]
    start = datetime(2026, 11, 24, 8, 0)
    for i in range(n):
        ip = random.choice(ips)
        if ip == "45.33.10.99":                         # an attacker hammering /login
            path, status = "/login", random.choice([401, 401, 401, 200])
        else:
            path, status = random.choice(pages), random.choices([200, 304, 404, 500], [85, 8, 5, 2])[0]
        ts = start + timedelta(seconds=i * random.randint(20, 80))
        yield f'{ip} - - [{ts:%d/%b/%Y:%H:%M:%S} +0530] "GET {path} HTTP/1.1" {status} {random.randint(200, 9000)}'

def analyze(lines):
    entries = [m.groupdict() for line in lines if (m := LOG_RE.search(line))]
    status = Counter(e["status"] for e in entries)
    pages = Counter(e["path"] for e in entries)
    ips = Counter(e["ip"] for e in entries)
    hours = Counter(datetime.strptime(e["ts"].split()[0], "%d/%b/%Y:%H:%M:%S").hour for e in entries)
    fails = defaultdict(int)
    for e in entries:
        if e["status"] == "401":
            fails[e["ip"]] += 1
    traffic = sum(int(e["size"]) for e in entries)

    print(f"📜 {len(entries)} requests | {traffic / 1e6:.2f} MB served")
    print("\nStatus codes:", dict(sorted(status.items())))
    err = sum(v for k, v in status.items() if k.startswith(("4", "5"))) / len(entries)
    print(f"Error rate: {err:.1%}")
    print("\nTop pages:")
    for p, c in pages.most_common(5):
        print(f"   {p:<20}{c:>5}")
    print("\nRequests by hour:")
    for h in sorted(hours):
        print(f"   {h:02d}:00 {'█' * (hours[h] // 4)} {hours[h]}")
    print("\n🚨 Suspicious IPs (5 or more failed logins):")
    for ip, n in sorted(fails.items(), key=lambda x: -x[1]):
        if n >= 5:
            print(f"   {ip}: {n} failed logins out of {ips[ip]} requests -> consider blocking")

if __name__ == "__main__":
    if DEMO or len(sys.argv) < 2:
        if not DEMO:
            print("Usage: python main.py access.log   (running on sample data now)\n")
        analyze(fake_logs())
    else:
        with open(sys.argv[1], encoding="utf-8", errors="ignore") as f:
            analyze(f)
```

## Extend this project

1. Export the report as HTML with a table.
2. Detect traffic spikes (more than 3× the average requests in a minute).
3. Follow a live log like `tail -f` and alert in real time.

---

[⬅ Day 153](../Day-153-Project-Duplicate-File-Finder/README.md) · [🏠 Home](../README.md) · [Day 155 ➡](../Day-155-Project-Markdown-to-HTML-Converter/README.md)
