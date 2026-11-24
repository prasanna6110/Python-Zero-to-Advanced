# 114 · Capstone Projects II: Systems

## Systems-level projects
| Project | Concepts used |
|---------|---------------|
| 1. Key-Value Database Server | sockets, threads, locks, a text protocol, persistence, a client |
| 2. Async Web Crawler (simulated) | asyncio, semaphores, queues, retries with backoff, contextvars-style logging |
| 3. Mini Web Framework | decorators, regex routing, WSGI, closures, a request/response model |

These are portfolio-worthy. Push each one to GitHub as its own repository with a README and tests.

## Examples

### Example 1: Key-Value Database Server (like a mini Redis)  ([`example_1.py`](example_1.py))

```python
import socket, threading, json, os

class KVServer:
    def __init__(self, snapshot="kv_snapshot.json"):
        self.data, self.lock, self.snapshot = {}, threading.Lock(), snapshot
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("127.0.0.1", 0)); self.sock.listen()
        self.port = self.sock.getsockname()[1]

    def handle(self, conn):
        with conn, conn.makefile("rw") as f:
            for line in f:
                parts = line.strip().split(" ", 2)
                cmd = parts[0].upper()
                with self.lock:
                    match cmd, parts[1:]:
                        case "SET", [key, value]: self.data[key] = value; reply = "OK"
                        case "GET", [key]: reply = self.data.get(key, "(nil)")
                        case "DEL", [key]: reply = str(int(self.data.pop(key, None) is not None))
                        case "INCR", [key]:
                            self.data[key] = str(int(self.data.get(key, "0")) + 1); reply = self.data[key]
                        case "KEYS", []: reply = ",".join(sorted(self.data)) or "(empty)"
                        case "SAVE", []:
                            with open(self.snapshot, "w") as s: json.dump(self.data, s)
                            reply = "SAVED"
                        case _: reply = "ERR unknown command"
                f.write(reply + "\n"); f.flush()

    def serve(self):
        while True:
            try:
                conn, _ = self.sock.accept()
            except OSError:
                break
            threading.Thread(target=self.handle, args=(conn,), daemon=True).start()

def client(port, *commands):
    with socket.create_connection(("127.0.0.1", port)) as s, s.makefile("rw") as f:
        for c in commands:
            f.write(c + "\n"); f.flush()
            print(f"  {c:<22} -> {f.readline().strip()}")

server = KVServer()
threading.Thread(target=server.serve, daemon=True).start()
print("client 1:")
client(server.port, "SET user:1 Prasanna", "SET course python", "GET user:1", "INCR visits", "INCR visits")
print("client 2 (sees the same data):")
counters = [threading.Thread(target=client, args=(server.port, "INCR visits")) for _ in range(3)]
for t in counters: t.start()
for t in counters: t.join()
client(server.port, "GET visits", "KEYS", "DEL course", "FOO", "SAVE")
server.sock.close()
print("snapshot on disk:", open(server.snapshot).read())
os.remove(server.snapshot)
```

### Example 2: Async Web Crawler (simulated network)  ([`example_2.py`](example_2.py))

```python
import asyncio, random, time
from urllib.parse import urljoin

random.seed(11)
FAKE_WEB = {
    "https://site.com/": ["/about", "/blog", "/shop"],
    "https://site.com/about": ["/team", "/"],
    "https://site.com/blog": ["/blog/python", "/blog/asyncio", "/broken"],
    "https://site.com/shop": ["/shop/cart"],
    "https://site.com/team": [], "https://site.com/blog/python": ["/blog/asyncio"],
    "https://site.com/blog/asyncio": [], "https://site.com/shop/cart": [],
}

async def fetch(url):
    await asyncio.sleep(random.uniform(0.05, 0.2))
    if url.endswith("/broken"):
        raise ConnectionError("404")
    if random.random() < 0.2:
        raise TimeoutError("flaky network")
    return FAKE_WEB[url]

async def fetch_with_retry(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            return await fetch(url)
        except TimeoutError:
            await asyncio.sleep(0.05 * 2 ** attempt)          # exponential backoff
    raise TimeoutError(f"gave up on {url}")

async def crawl(start, max_concurrency=3, workers=4):
    queue, seen, results = asyncio.Queue(), {start}, {}
    sem = asyncio.Semaphore(max_concurrency)
    await queue.put(start)

    async def worker(name):
        while True:
            url = await queue.get()
            try:
                async with sem:
                    links = await fetch_with_retry(url)
                results[url] = f"ok ({len(links)} links)"
                for link in links:
                    full = urljoin(url, link)
                    if full not in seen:
                        seen.add(full); await queue.put(full)
            except Exception as e:
                results[url] = f"error: {e}"
            finally:
                queue.task_done()

    tasks = [asyncio.create_task(worker(f"w{i}")) for i in range(workers)]
    await queue.join()
    for t in tasks: t.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    return results

start = time.perf_counter()
report = asyncio.run(crawl("https://site.com/"))
for url, status in sorted(report.items()):
    print(f"{url:<32} {status}")
print(f"crawled {len(report)} pages in {time.perf_counter() - start:.2f}s")
```

### Example 3: Mini Web Framework (WSGI + decorator routing)  ([`example_3.py`](example_3.py))

```python
import re, json, io
from wsgiref.util import setup_testing_defaults

class Request:
    def __init__(self, environ):
        self.method = environ["REQUEST_METHOD"]
        self.path = environ["PATH_INFO"]
        size = int(environ.get("CONTENT_LENGTH") or 0)
        self.body = environ["wsgi.input"].read(size) if size else b""
    def json(self):
        return json.loads(self.body or b"{}")

class MiniFramework:
    def __init__(self):
        self.routes = []
        self.middlewares = []

    def route(self, pattern, methods=("GET",)):
        regex = re.compile("^" + re.sub(r"<(\w+)>", r"(?P<\1>[^/]+)", pattern) + "$")
        def decorator(handler):
            self.routes.append((regex, methods, handler))
            return handler
        return decorator

    def middleware(self, fn):
        self.middlewares.append(fn); return fn

    def __call__(self, environ, start_response):          # the WSGI entry point
        req = Request(environ)
        for regex, methods, handler in self.routes:
            if (m := regex.match(req.path)) and req.method in methods:
                status, body = "200 OK", handler(req, **m.groupdict())
                break
        else:
            status, body = "404 Not Found", {"error": f"no route for {req.method} {req.path}"}
        for mw in self.middlewares:
            body = mw(req, body)
        data = json.dumps(body).encode()
        start_response(status, [("Content-Type", "application/json")])
        return [data]

app = MiniFramework()
USERS = {"1": {"name": "Prasanna", "college": "NIT Kurukshetra"}}

@app.route("/")
def home(req): return {"message": "Welcome to MiniFramework"}

@app.route("/users/<uid>")
def get_user(req, uid): return USERS.get(uid, {"error": "not found"})

@app.route("/users", methods=("POST",))
def create_user(req):
    uid = str(len(USERS) + 1); USERS[uid] = req.json(); return {"created": uid}

@app.middleware
def add_meta(req, body): return {**body, "_path": req.path}

def call(method, path, payload=None):
    environ = {}
    setup_testing_defaults(environ)
    data = json.dumps(payload).encode() if payload else b""
    environ.update(REQUEST_METHOD=method, PATH_INFO=path, CONTENT_LENGTH=str(len(data)),
                   **{"wsgi.input": io.BytesIO(data)})
    result = {}
    body = app(environ, lambda status, headers: result.update(status=status))
    print(f"{method:<5}{path:<12} {result['status']:<14} {b''.join(body).decode()}")

call("GET", "/")
call("GET", "/users/1")
call("POST", "/users", {"name": "Asha"})
call("GET", "/users/2")
call("GET", "/nope")
print("\nTo serve for real: from wsgiref.simple_server import make_server; make_server('', 8000, app).serve_forever()")
```

## Practice

1. KV server: add a `TTL key seconds` command for keys that expire, plus pub/sub.
2. Crawler: use real `aiohttp` and respect `robots.txt`.
3. Framework: add templates, query-string parsing and serve it with `wsgiref`.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
