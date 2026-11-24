# Day 120 · Advanced Structural Pattern Matching — Matching nested JSON events
# Run: python example_2.py

events = [
    {"type": "push", "repo": "course", "commits": [{"msg": "add day 1"}, {"msg": "fix typo"}]},
    {"type": "issue", "action": "opened", "user": {"login": "asha", "roles": ["member", "admin"]}},
    {"type": "issue", "action": "closed", "user": {"login": "ravi", "roles": ["member"]}},
    {"type": "star", "count": 1000, "extra": "ignored"},
    {"type": "unknown"},
]

def handle(event):
    match event:
        case {"type": "push", "commits": [{"msg": first}, *rest]}:
            return f"push: '{first}' + {len(rest)} more commits"
        case {"type": "issue", "action": "opened", "user": {"login": login, "roles": [*roles]}} if "admin" in roles:
            return f"issue opened by admin {login}"
        case {"type": "issue", "action": action, "user": {"login": login}}:
            return f"issue {action} by {login}"
        case {"type": "star", "count": int(n), **rest} if n >= 1000:
            return f"milestone: {n} stars! (other keys: {list(rest)})"
        case {"type": t}:
            return f"unhandled event type {t!r}"

for e in events:
    print(handle(e))
