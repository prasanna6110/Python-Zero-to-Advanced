# Day 167 · Project: Blockchain from Scratch — Mini Blockchain with Proof of Work
# Run: python main.py

import hashlib
import json
import time
from dataclasses import dataclass, field, asdict

DIFFICULTY = 4                      # the hash must start with this many zeros

@dataclass
class Block:
    index: int
    transactions: list
    previous_hash: str
    timestamp: float = field(default_factory=time.time)
    nonce: int = 0
    hash: str = ""

    def compute_hash(self):
        data = {k: v for k, v in asdict(self).items() if k != "hash"}
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def mine(self):
        start = time.perf_counter()
        while not (h := self.compute_hash()).startswith("0" * DIFFICULTY):
            self.nonce += 1
        self.hash = h
        return time.perf_counter() - start

class Blockchain:
    REWARD = 50
    def __init__(self):
        genesis = Block(0, [{"from": "network", "to": "genesis", "amount": 0}], "0" * 64)
        genesis.mine()
        self.chain, self.pending = [genesis], []

    def add_transaction(self, sender, receiver, amount):
        if sender != "network" and self.balance(sender) < amount:
            raise ValueError(f"{sender} has insufficient balance ({self.balance(sender)})")
        self.pending.append({"from": sender, "to": receiver, "amount": amount})

    def mine_pending(self, miner):
        txs = self.pending + [{"from": "network", "to": miner, "amount": self.REWARD}]
        block = Block(len(self.chain), txs, self.chain[-1].hash)
        seconds = block.mine()
        self.chain.append(block)
        self.pending = []
        print(f"⛏️  Block {block.index} mined by {miner} in {seconds:.2f}s, nonce={block.nonce}, hash={block.hash[:16]}...")

    def balance(self, who):
        bal = 0
        for b in self.chain:
            for t in b.transactions:
                bal += t["amount"] if t["to"] == who else 0
                bal -= t["amount"] if t["from"] == who else 0
        return bal

    def is_valid(self):
        for prev, cur in zip(self.chain, self.chain[1:]):
            if cur.hash != cur.compute_hash():
                return False, f"block {cur.index} data was tampered with"
            if cur.previous_hash != prev.hash:
                return False, f"block {cur.index} isn't linked to block {prev.index}"
            if not cur.hash.startswith("0" * DIFFICULTY):
                return False, f"block {cur.index} wasn't mined"
        return True, "chain is valid ✅"

if __name__ == "__main__":
    coin = Blockchain()
    coin.mine_pending("Prasanna")
    coin.add_transaction("Prasanna", "Asha", 20)
    coin.add_transaction("Prasanna", "Ravi", 5)
    coin.mine_pending("Asha")
    try:
        coin.add_transaction("Ravi", "Meera", 100)
    except ValueError as e:
        print("❌", e)
    for who in ["Prasanna", "Asha", "Ravi"]:
        print(f"💰 {who}: {coin.balance(who)} coins")
    print(coin.is_valid())
    print("\n😈 A hacker changes the amount in block 2...")
    coin.chain[2].transactions[0]["amount"] = 2000
    print(coin.is_valid())
    print("😈 ...and recomputes that block's hash...")
    coin.chain[2].hash = coin.chain[2].compute_hash()
    print(coin.is_valid())
