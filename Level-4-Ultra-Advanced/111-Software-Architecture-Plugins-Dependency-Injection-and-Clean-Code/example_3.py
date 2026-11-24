# 111 · Software Architecture: Plugins, Dependency Injection and Clean Code — Example 3: Typed settings from environment variables
# Run: python example_3.py

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
