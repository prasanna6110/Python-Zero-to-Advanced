# Day 166 · Project: REST API for a To-Do App (http.server + SQLite) — To-Do REST API
# Run: python main.py

import json
import re
import sqlite3
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import Request, urlopen
from urllib.error import HTTPError

DEMO = not sys.stdin.isatty()
db = sqlite3.connect(":memory:" if DEMO else "todos.db", check_same_thread=False)
db.row_factory = sqlite3.Row
db.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER DEFAULT 0)")
lock = threading.Lock()

class API(BaseHTTPRequestHandler):
    def reply(self, status, data=None):
        body = json.dumps(data).encode() if data is not None else b""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def body(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}")

    def route(self, method):
        m = re.fullmatch(r"/todos(?:/(\d+))?", self.path)
        if not m:
            return self.reply(404, {"error": "not found"})
        tid = m.group(1)
        with lock, db:
            if method == "GET" and tid is None:
                return self.reply(200, [dict(r) for r in db.execute("SELECT * FROM todos")])
            if method == "POST" and tid is None:
                data = self.body()
                if not data.get("title"):
                    return self.reply(400, {"error": "title is required"})
                cur = db.execute("INSERT INTO todos (title, done) VALUES (?, ?)", (data["title"], int(data.get("done", 0))))
                return self.reply(201, {"id": cur.lastrowid, "title": data["title"], "done": int(data.get("done", 0))})
            row = db.execute("SELECT * FROM todos WHERE id=?", (tid,)).fetchone() if tid else None
            if row is None:
                return self.reply(404, {"error": f"todo {tid} not found"})
            if method == "GET":
                return self.reply(200, dict(row))
            if method == "PUT":
                data = {**dict(row), **self.body()}
                db.execute("UPDATE todos SET title=?, done=? WHERE id=?", (data["title"], int(data["done"]), tid))
                return self.reply(200, {"id": int(tid), "title": data["title"], "done": int(data["done"])})
            if method == "DELETE":
                db.execute("DELETE FROM todos WHERE id=?", (tid,))
                return self.reply(204)
        self.reply(405, {"error": "method not allowed"})

    do_GET = lambda self: self.route("GET")
    do_POST = lambda self: self.route("POST")
    do_PUT = lambda self: self.route("PUT")
    do_DELETE = lambda self: self.route("DELETE")
    def log_message(self, fmt, *args):
        if not DEMO:
            super().log_message(fmt, *args)

def call(base, method, path, data=None):
    req = Request(base + path, method=method, data=json.dumps(data).encode() if data else None,
                  headers={"Content-Type": "application/json"})
    try:
        with urlopen(req) as r:
            status, text = r.status, r.read().decode()
    except HTTPError as e:
        status, text = e.code, e.read().decode()
    print(f"{method:<6} {path:<10} -> {status} {text}")

if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 0 if DEMO else 8000), API)
    base = f"http://127.0.0.1:{server.server_address[1]}"
    if DEMO:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        call(base, "POST", "/todos", {"title": "Learn REST APIs"})
        call(base, "POST", "/todos", {"title": "Push project to GitHub"})
        call(base, "POST", "/todos", {})
        call(base, "GET", "/todos")
        call(base, "PUT", "/todos/1", {"done": True})
        call(base, "DELETE", "/todos/2")
        call(base, "GET", "/todos/2")
        call(base, "GET", "/todos")
        server.shutdown()
    else:
        print(f"🚀 API running at {base}/todos  (try: curl {base}/todos)")
        server.serve_forever()
