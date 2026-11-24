# 109 · Advanced Concurrency Patterns — Example 2: The actor model with threads and queues
# Run: python example_2.py

import threading, queue

class Actor(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.mailbox = queue.Queue()
    def send(self, msg):
        self.mailbox.put(msg)
    def run(self):
        while (msg := self.mailbox.get()) is not None:
            self.receive(msg)
    def stop(self):
        self.mailbox.put(None); self.join()

class BankAccount(Actor):
    def __init__(self):
        super().__init__(); self.balance = 0
    def receive(self, msg):
        match msg:
            case ("deposit", amt): self.balance += amt
            case ("withdraw", amt) if amt <= self.balance: self.balance -= amt
            case ("balance", reply_q): reply_q.put(self.balance)

acct = BankAccount(); acct.start()
workers = [threading.Thread(target=lambda: [acct.send(("deposit", 1)) for _ in range(1000)]) for _ in range(5)]
for w in workers: w.start()
for w in workers: w.join()
acct.send(("withdraw", 300))
reply = queue.Queue(); acct.send(("balance", reply))
print("final balance (no locks needed):", reply.get())
acct.stop()
