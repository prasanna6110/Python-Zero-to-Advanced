# Day 099 · Networking: Sockets, HTTP and urllib

_Advanced_

## Sockets: the lowest level of networking
- **TCP** (`SOCK_STREAM`): reliable, ordered and connection-based (HTTP, SSH).
- **UDP** (`SOCK_DGRAM`): fast and connectionless (DNS, games, video).

Server: `socket()` → `bind()` → `listen()` → `accept()` → `recv()/send()`
Client: `socket()` → `connect()` → `send()/recv()`

## HTTP in the standard library
- `http.server`: a simple web server (`python -m http.server 8000` serves the current folder).
- `urllib.request`: makes HTTP requests. `urllib.parse` builds and parses URLs.
- In real projects, use **requests** or **httpx** for clients and **FastAPI** or **Flask** for servers.

## Methods and status codes
GET (read), POST (create), PUT/PATCH (update), DELETE.
Status codes: 2xx success, 3xx redirect, 4xx client error, 5xx server error.

## Examples

### Example 1: TCP echo server and client (localhost)  ([`example_1.py`](example_1.py))

```python
import socket, threading

def server(sock):
    conn, addr = sock.accept()
    with conn:
        while data := conn.recv(1024):
            conn.sendall(b"ECHO: " + data.upper())

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))            # port 0 = pick any free port
srv.listen()
port = srv.getsockname()[1]
threading.Thread(target=server, args=(srv,), daemon=True).start()

with socket.create_connection(("127.0.0.1", port)) as client:
    for msg in [b"hello", b"python sockets"]:
        client.sendall(msg)
        print(client.recv(1024).decode())
srv.close()
```

### Example 2: A tiny HTTP JSON API with http.server and urllib  ([`example_2.py`](example_2.py))

```python
import json, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen, Request

class API(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"path": self.path, "message": "Hello from Python"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = json.loads(self.rfile.read(length))
        self.send_response(201); self.end_headers()
        self.wfile.write(json.dumps({"received": data}).encode())
    def log_message(self, *args):
        pass

httpd = HTTPServer(("127.0.0.1", 0), API)
port = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()

with urlopen(f"http://127.0.0.1:{port}/users/1") as r:
    print(r.status, json.loads(r.read()))
req = Request(f"http://127.0.0.1:{port}/users", data=json.dumps({"name": "Asha"}).encode(),
              headers={"Content-Type": "application/json"}, method="POST")
with urlopen(req) as r:
    print(r.status, json.loads(r.read()))
httpd.shutdown()
```

### Example 3: URL parsing and UDP  ([`example_3.py`](example_3.py))

```python
from urllib.parse import urlparse, parse_qs, urlencode, quote
import socket

url = "https://shop.example.com:8443/search?q=python+book&page=2#results"
p = urlparse(url)
print(p.scheme, p.hostname, p.port, p.path, parse_qs(p.query), p.fragment)
print("build:", "https://api.site.com/items?" + urlencode({"q": "नमस्ते", "limit": 10}))
print("quote:", quote("file name.pdf"))

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(("127.0.0.1", 0))
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.sendto(b"udp packet!", receiver.getsockname())
data, addr = receiver.recvfrom(1024)
print("UDP received:", data, "from", addr[0])
sender.close(); receiver.close()
```

## Practice

1. Build a multi-client chat server with sockets and threads.
2. Add a `/time` endpoint to the HTTP server.
3. Write a port checker that tests whether localhost ports 8000 to 8010 are open.

---

[⬅ Day 098](../Day-098-Databases-with-sqlite3/README.md) · [🏠 Home](../README.md) · [Day 100 ➡](../Day-100-Web-Scraping-and-HTML-Parsing/README.md)
