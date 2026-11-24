# Day 099 · Networking: Sockets, HTTP and urllib — TCP echo server and client (localhost)
# Run: python example_1.py

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
