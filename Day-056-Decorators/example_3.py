# Day 056 · Decorators — Stacking decorators and access control
# Run: python example_3.py

import functools

current_user = {"name": "prasanna", "role": "admin"}

def require_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if current_user["role"] != "admin":
            raise PermissionError("admins only")
        return func(*args, **kwargs)
    return wrapper

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

@bold
@require_admin
def delete_user(name):
    return f"deleted {name}"

print(delete_user("spammer"))
current_user["role"] = "guest"
try:
    delete_user("someone")
except PermissionError as e:
    print("Blocked:", e)
