# Day 162 · Project: Key-Value Database Server (Mini Redis)

_Projects_

**Concepts:** TCP sockets, one thread per client, locks, a text protocol parsed with `match`, JSON snapshots.

A tiny Redis-like server: `SET`, `GET`, `DEL`, `INCR`, `KEYS`, `SAVE`. Several clients can connect at the same time.

## Code

### Key-Value Database Server (Mini Redis)  ([`main.py`](main.py))

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

## Extend this project

1. Add a `TTL key seconds` command for keys that expire.
2. Add `PUBLISH`/`SUBSCRIBE` channels.
3. Write an append-only log for durability.

---

[⬅ Day 161](../Day-161-Project-Loan-EMI-Calculator-with-Amortization-Schedule/README.md) · [🏠 Home](../README.md) · [Day 163 ➡](../Day-163-Project-Async-Web-Crawler/README.md)
