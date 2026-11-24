# 102 · Advanced Metaprogramming: Code Generation and Function Objects — Example 3: Module __getattr__ and a dynamic API client
# Run: python example_3.py

import sys, types, warnings

mod = types.ModuleType("config_mod")
exec('''
import warnings
_settings = {"timeout": 30, "retries": 3}
def __getattr__(name):
    if name == "TIMEOUT_OLD":
        warnings.warn("TIMEOUT_OLD is deprecated, use timeout", DeprecationWarning)
        return _settings["timeout"]
    if name in _settings:
        return _settings[name]
    raise AttributeError(f"module has no attribute {name!r}")
''', mod.__dict__)
sys.modules["config_mod"] = mod
import config_mod
print(config_mod.timeout, config_mod.retries)
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    print(config_mod.TIMEOUT_OLD, "| warning:", w[0].message)

class APIClient:
    """Any attribute chain becomes a URL path: client.users.list() -> GET /users/list"""
    def __init__(self, path=""):
        self._path = path
    def __getattr__(self, name):
        return APIClient(f"{self._path}/{name}")
    def __call__(self, **params):
        q = "&".join(f"{k}={v}" for k, v in params.items())
        return f"GET {self._path}" + (f"?{q}" if q else "")

api = APIClient()
print(api.users.list(page=2))
print(api.repos.prasanna6110.issues())
