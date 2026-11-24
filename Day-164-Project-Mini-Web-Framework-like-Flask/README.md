# Day 164 · Project: Mini Web Framework (like Flask)

_Projects_

**Concepts:** WSGI, decorators for routing, regex URL parameters, middleware, JSON responses.

Build your own Flask-like framework in about 70 lines and understand how real web frameworks work inside.

## Code

### Mini Web Framework (like Flask)  ([`main.py`](main.py))

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

## Extend this project

1. Add query-string parsing and HTML templates.
2. Serve it for real with `wsgiref.simple_server`.
3. Add sessions with signed cookies (`hmac`).

---

[⬅ Day 163](../Day-163-Project-Async-Web-Crawler/README.md) · [🏠 Home](../README.md) · [Day 165 ➡](../Day-165-Project-Multi-Client-Chat-Server/README.md)
