# Day 156 · Project: URL Shortener (SQLite + Base62)

_Projects_

**Concepts:** base62 encoding, SQLite, URL validation, click counting, an HTTP redirect server with `http.server`.

Like bit.ly: it turns long URLs into short codes, redirects visitors and keeps statistics.

## Code

### URL Shortener with a Redirect Server  ([`main.py`](main.py))

```python
import sqlite3
import string
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib.request import urlopen, Request, HTTPRedirectHandler, build_opener

DEMO = not sys.stdin.isatty()
ALPHABET = string.digits + string.ascii_letters

def base62(n):
    s = ""
    while True:
        n, r = divmod(n, 62)
        s = ALPHABET[r] + s
        if n == 0:
            return s

class Shortener:
    def __init__(self, db=":memory:"):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.lock = threading.Lock()
        self.conn.execute("CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, code TEXT UNIQUE, url TEXT, clicks INT DEFAULT 0)")

    def shorten(self, url, custom=None):
        p = urlparse(url)
        if p.scheme not in ("http", "https") or not p.netloc:
            raise ValueError(f"invalid URL: {url}")
        with self.lock, self.conn:
            row = self.conn.execute("SELECT code FROM urls WHERE url=?", (url,)).fetchone()
            if row:
                return row[0]
            cur = self.conn.execute("INSERT INTO urls (url) VALUES (?)", (url,))
            code = custom or base62(cur.lastrowid + 100_000)      # offset so codes aren't 1, 2, 3...
            self.conn.execute("UPDATE urls SET code=? WHERE id=?", (code, cur.lastrowid))
            return code

    def resolve(self, code):
        with self.lock, self.conn:
            row = self.conn.execute("SELECT url FROM urls WHERE code=?", (code,)).fetchone()
            if row:
                self.conn.execute("UPDATE urls SET clicks = clicks + 1 WHERE code=?", (code,))
            return row[0] if row else None

    def stats(self):
        return self.conn.execute("SELECT code, url, clicks FROM urls ORDER BY clicks DESC").fetchall()

def make_server(shortener):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            url = shortener.resolve(self.path.lstrip("/"))
            if url:
                self.send_response(302); self.send_header("Location", url); self.end_headers()
            else:
                self.send_response(404); self.end_headers(); self.wfile.write(b"Short link not found")
        def log_message(self, *a): pass
    return HTTPServer(("127.0.0.1", 0 if DEMO else 8080), Handler)

if __name__ == "__main__":
    s = Shortener()
    server = make_server(s)
    host = f"http://127.0.0.1:{server.server_address[1]}"
    threading.Thread(target=server.serve_forever, daemon=True).start()
    urls = ["https://github.com/prasanna6110/Python-Zero-to-Ultra-Advanced",
            "https://docs.python.org/3/library/asyncio.html", "https://nitkkr.ac.in", "not-a-url"]
    if not DEMO:
        urls = [input("Long URL: ")]
    for u in urls:
        try:
            print(f"🔗 {host}/{s.shorten(u)}  <-  {u}")
        except ValueError as e:
            print("❌", e)

    class NoRedirect(HTTPRedirectHandler):
        def redirect_request(self, *a, **k): return None
    opener = build_opener(NoRedirect)
    for code in [s.shorten(urls[0])] * 3 + ["zzz"]:
        try:
            opener.open(f"{host}/{code}")
        except Exception as e:
            print(f"GET /{code} -> {e.code} {e.headers.get('Location', '')}")
    print("\n📊 Stats:", *(f"\n   {c}: {n} clicks  {u[:45]}" for c, u, n in s.stats()))
    if not DEMO:
        print(f"\nServer running at {host}. Open a short link in your browser. Ctrl+C to stop.")
        try:
            threading.Event().wait()
        except KeyboardInterrupt:
            pass
    server.shutdown()
```

## Extend this project

1. Add an HTML form at `/` for creating links.
2. Add an expiry date for each link.
3. Track click timestamps and the referrer in another table.

---

[⬅ Day 155](../Day-155-Project-Markdown-to-HTML-Converter/README.md) · [🏠 Home](../README.md) · [Day 157 ➡](../Day-157-Project-Conway-s-Game-of-Life/README.md)
