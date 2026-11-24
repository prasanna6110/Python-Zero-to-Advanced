# Day 165 · Project: Multi-Client Chat Server

_Projects_

**Concepts:** TCP sockets, a thread for each client, a shared client list protected by a lock, broadcasting, chat commands (`/nick`, `/list`, `/msg`, `/quit`).

Run `python main.py server` in one terminal and `python main.py client` in several others to chat with each other on your local network.

## Code

### Chat Server and Client  ([`main.py`](main.py))

```python
import socket
import sys
import threading
import time

HOST, PORT = "127.0.0.1", 5050

class ChatServer:
    def __init__(self, host=HOST, port=PORT):
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port)); self.sock.listen()
        self.port = self.sock.getsockname()[1]
        self.clients, self.lock = {}, threading.Lock()       # conn -> nickname

    def broadcast(self, msg, exclude=None):
        with self.lock:
            for c in list(self.clients):
                if c is not exclude:
                    try:
                        c.sendall((msg + "\n").encode())
                    except OSError:
                        self.clients.pop(c, None)

    def handle(self, conn):
        f = conn.makefile("r")
        with self.lock:
            nick = f"user{len(self.clients) + 1}"
            self.clients[conn] = nick
        conn.sendall(f"Welcome {nick}! Commands: /nick NAME, /list, /msg NAME TEXT, /quit\n".encode())
        self.broadcast(f"📢 {nick} joined", exclude=conn)
        for line in f:
            text = line.strip()
            match text.split(" ", 2):
                case ["/nick", new]:
                    old, self.clients[conn] = self.clients[conn], new
                    self.broadcast(f"✏️  {old} is now {new}")
                case ["/list"]:
                    conn.sendall(("Online: " + ", ".join(self.clients.values()) + "\n").encode())
                case ["/msg", to, body]:
                    target = next((c for c, n in self.clients.items() if n == to), None)
                    if target:
                        target.sendall(f"🔒 {self.clients[conn]} -> you: {body}\n".encode())
                    else:
                        conn.sendall(f"No user {to}\n".encode())
                case ["/quit"]:
                    break
                case _ if text:
                    self.broadcast(f"[{self.clients[conn]}] {text}", exclude=conn)
        with self.lock:
            nick = self.clients.pop(conn, "someone")
        self.broadcast(f"👋 {nick} left")
        conn.close()

    def serve(self):
        while True:
            try:
                conn, _ = self.sock.accept()
            except OSError:
                return
            threading.Thread(target=self.handle, args=(conn,), daemon=True).start()

def client(port=PORT):
    s = socket.create_connection((HOST, port))
    def receive():
        for line in s.makefile("r"):
            print("\r" + line.strip() + "\n> ", end="")
    threading.Thread(target=receive, daemon=True).start()
    try:
        while (msg := input("> ")) is not None:
            s.sendall((msg + "\n").encode())
            if msg == "/quit":
                break
    except (EOFError, KeyboardInterrupt):
        pass
    s.close()

def demo():
    server = ChatServer(port=0)
    threading.Thread(target=server.serve, daemon=True).start()
    logs = {}
    def bot(name, messages):
        s = socket.create_connection((HOST, server.port))
        f = s.makefile("r")
        logs[name] = []
        threading.Thread(target=lambda: [logs[name].append(l.strip()) for l in f], daemon=True).start()
        for m in messages:
            time.sleep(0.15); s.sendall((m + "\n").encode())
        time.sleep(0.4); s.close()
    bots = [threading.Thread(target=bot, args=("A", ["/nick Prasanna", "Hello everyone!", "/msg Asha see you in the lab", "/list"])),
            threading.Thread(target=bot, args=("B", ["/nick Asha", "Hi Prasanna 👋", "bye"]))]
    for b in bots: b.start(); time.sleep(0.05)
    for b in bots: b.join()
    for name, lines in logs.items():
        print(f"--- what client {name} saw ---")
        print("\n".join(lines))
    server.sock.close()

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ("demo" if not sys.stdin.isatty() else "")
    if mode == "server":
        print(f"💬 Chat server on {HOST}:{PORT}"); ChatServer().serve()
    elif mode == "client":
        client()
    else:
        demo()
```

## Extend this project

1. Add chat rooms (`/join python`).
2. Save the chat history to SQLite and send the last 10 messages to anyone who joins.
3. Rewrite the server with `asyncio.start_server`.

---

[⬅ Day 164](../Day-164-Project-Mini-Web-Framework-like-Flask/README.md) · [🏠 Home](../README.md) · [Day 166 ➡](../Day-166-Project-REST-API-for-a-To-Do-App-http-server-SQLite/README.md)
