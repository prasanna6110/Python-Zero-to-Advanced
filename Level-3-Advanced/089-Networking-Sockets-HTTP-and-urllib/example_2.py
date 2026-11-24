# 089 · Networking: Sockets, HTTP and urllib — Example 2: A tiny HTTP JSON API with http.server and urllib
# Run: python example_2.py

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
