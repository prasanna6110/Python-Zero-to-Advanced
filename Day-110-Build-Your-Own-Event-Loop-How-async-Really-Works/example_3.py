# Day 110 · Build Your Own Event Loop (How async Really Works) — A non-blocking socket server using selectors (what asyncio uses)
# Run: python example_3.py

import selectors, socket, threading, time

sel = selectors.DefaultSelector()
server = socket.socket()
server.bind(("127.0.0.1", 0)); server.listen(); server.setblocking(False)
port = server.getsockname()[1]
sel.register(server, selectors.EVENT_READ, data=None)

def run_server(max_msgs):
    handled = 0
    while handled < max_msgs:
        for key, _ in sel.select(timeout=1):
            if key.data is None:                       # a new connection
                conn, _ = key.fileobj.accept()
                conn.setblocking(False)
                sel.register(conn, selectors.EVENT_READ, data="client")
            else:                                      # a client sent data
                data = key.fileobj.recv(1024)
                if data:
                    key.fileobj.sendall(b"pong:" + data); handled += 1
                else:
                    sel.unregister(key.fileobj); key.fileobj.close()

t = threading.Thread(target=run_server, args=(3,), daemon=True); t.start()
clients = [socket.create_connection(("127.0.0.1", port)) for _ in range(3)]
for i, c in enumerate(clients):
    c.sendall(f"client{i}".encode())
for c in clients:
    print(c.recv(1024).decode()); c.close()
t.join(2); server.close()
print("One thread served 3 clients concurrently using selectors.")
