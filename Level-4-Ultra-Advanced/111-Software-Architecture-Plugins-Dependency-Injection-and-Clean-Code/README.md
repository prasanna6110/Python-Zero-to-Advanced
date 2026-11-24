# 111 · Software Architecture: Plugins, Dependency Injection and Clean Code

## Building large Python applications
- **Layered / clean architecture**: domain (pure business logic) → services (use cases) → adapters (database, web, CLI). Dependencies point **inwards**.
- **Dependency injection (DI)**: pass dependencies in (through the constructor or function arguments) instead of creating them inside. That makes the code testable and swappable.
- **Interfaces with Protocols**: depend on abstractions, not concrete classes.
- **Plugin systems**: registries, `importlib.metadata.entry_points` (how pytest plugins and Flask extensions work), or folder discovery.
- **Configuration**: environment variables or `.env` files, plus a typed settings object, with no secrets in the code.

## Project structure
```
app/
  domain/      # entities and rules, no I/O
  services/    # use cases
  adapters/    # db, http, email
  main.py      # wiring (composition root)
tests/
```

## Examples

### Example 1: Dependency injection with Protocols  ([`example_1.py`](example_1.py))

```python
from typing import Protocol
from dataclasses import dataclass

class Notifier(Protocol):
    def send(self, to: str, msg: str) -> None: ...

class UserRepo(Protocol):
    def save(self, user: dict) -> int: ...

@dataclass
class SignupService:                       # depends only on abstractions
    repo: UserRepo
    notifier: Notifier
    def signup(self, email: str) -> int:
        if "@" not in email:
            raise ValueError("invalid email")
        uid = self.repo.save({"email": email})
        self.notifier.send(email, f"Welcome! Your id is {uid}")
        return uid

class InMemoryRepo:
    def __init__(self): self.rows = []
    def save(self, user): self.rows.append(user); return len(self.rows)

class ConsoleNotifier:
    def send(self, to, msg): print(f"[email to {to}] {msg}")

class FakeNotifier:                        # for tests
    def __init__(self): self.sent = []
    def send(self, to, msg): self.sent.append((to, msg))

service = SignupService(InMemoryRepo(), ConsoleNotifier())
service.signup("prasanna@example.com")

fake = FakeNotifier()
test_service = SignupService(InMemoryRepo(), fake)
test_service.signup("t@test.com")
assert fake.sent[0][0] == "t@test.com"
print("test passed with the fake notifier:", fake.sent)
```

### Example 2: Plugin discovery from a folder and entry points  ([`example_2.py`](example_2.py))

```python
import importlib.util, pathlib, shutil, importlib.metadata as md

plugin_dir = pathlib.Path("plugins_demo")
plugin_dir.mkdir(exist_ok=True)
(plugin_dir / "uppercase.py").write_text("NAME='upper'\ndef apply(t): return t.upper()\n")
(plugin_dir / "reverse.py").write_text("NAME='reverse'\ndef apply(t): return t[::-1]\n")
(plugin_dir / "exclaim.py").write_text("NAME='exclaim'\ndef apply(t): return t + '!!!'\n")

def discover(folder):
    plugins = {}
    for file in sorted(folder.glob("*.py")):
        spec = importlib.util.spec_from_file_location(file.stem, file)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "apply"):
            plugins[mod.NAME] = mod.apply
    return plugins

plugins = discover(plugin_dir)
text = "python plugins"
for name, fn in plugins.items():
    text = fn(text)
    print(f"after {name:<8}: {text}")
shutil.rmtree(plugin_dir)

groups = md.entry_points()
print("installed console_scripts (first 5):", [ep.name for ep in groups.select(group="console_scripts")][:5])
```

### Example 3: Typed settings from environment variables  ([`example_3.py`](example_3.py))

```python
import os
from dataclasses import dataclass, fields

@dataclass(frozen=True)
class Settings:
    app_name: str = "course-app"
    debug: bool = False
    port: int = 8000
    db_url: str = "sqlite:///app.db"

    @classmethod
    def from_env(cls, prefix="APP_"):
        values = {}
        for f in fields(cls):
            raw = os.environ.get(prefix + f.name.upper())
            if raw is None:
                continue
            if f.type is bool:
                values[f.name] = raw.lower() in {"1", "true", "yes"}
            elif f.type is int:
                values[f.name] = int(raw)
            else:
                values[f.name] = raw
        return cls(**values)

os.environ["APP_DEBUG"] = "true"
os.environ["APP_PORT"] = "9090"
settings = Settings.from_env()
print(settings)
print("Never hard-code secrets; read them from the environment like this.")
```

## Practice

1. Restructure one of your projects into domain, services and adapters layers.
2. Write a plugin-based text processor that loads plugins from a folder.
3. Add a `.env` file loader (parse `KEY=VALUE` lines yourself).

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)
