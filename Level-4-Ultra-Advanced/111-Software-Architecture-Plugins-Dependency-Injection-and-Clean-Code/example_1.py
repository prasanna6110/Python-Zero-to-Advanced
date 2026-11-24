# 111 · Software Architecture: Plugins, Dependency Injection and Clean Code — Example 1: Dependency injection with Protocols
# Run: python example_1.py

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
