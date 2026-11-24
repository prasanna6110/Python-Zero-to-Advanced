# Day 168 · Project: Mini Version Control System (Like Git) — Mini Git
# Run: python main.py

import difflib
import hashlib
import json
import shutil
import sys
import tempfile
import time
import zlib
from pathlib import Path

class MiniGit:
    def __init__(self, root):
        self.root = Path(root)
        self.repo = self.root / ".minigit"

    def init(self):
        (self.repo / "objects").mkdir(parents=True, exist_ok=True)
        (self.repo / "HEAD").write_text("")
        print("Initialised an empty MiniGit repo")

    def _store(self, data: bytes):
        oid = hashlib.sha1(data).hexdigest()
        path = self.repo / "objects" / oid
        if not path.exists():
            path.write_bytes(zlib.compress(data))
        return oid

    def _load(self, oid):
        return zlib.decompress((self.repo / "objects" / oid).read_bytes())

    def _tracked_files(self):
        return sorted(p for p in self.root.rglob("*") if p.is_file() and ".minigit" not in p.parts)

    def head(self):
        return (self.repo / "HEAD").read_text() or None

    def commit(self, message):
        tree = {str(p.relative_to(self.root)): self._store(p.read_bytes()) for p in self._tracked_files()}
        parent = self.head()
        if parent and json.loads(self._load(parent))["tree"] == tree:
            print("Nothing to commit"); return parent
        commit = {"tree": tree, "parent": parent, "message": message, "time": time.time()}
        oid = self._store(json.dumps(commit, sort_keys=True).encode())
        (self.repo / "HEAD").write_text(oid)
        print(f"[{oid[:7]}] {message} ({len(tree)} files)")
        return oid

    def log(self):
        oid = self.head()
        while oid:
            c = json.loads(self._load(oid))
            print(f"commit {oid[:10]}  {time.strftime('%H:%M:%S', time.localtime(c['time']))}  {c['message']}")
            oid = c["parent"]

    def diff(self):
        tree = json.loads(self._load(self.head()))["tree"] if self.head() else {}
        for p in self._tracked_files():
            rel = str(p.relative_to(self.root))
            old = self._load(tree[rel]).decode().splitlines() if rel in tree else []
            new = p.read_text().splitlines()
            for line in difflib.unified_diff(old, new, f"a/{rel}", f"b/{rel}", lineterm=""):
                print("   " + line)

    def checkout(self, oid_prefix):
        oid = next(o.name for o in (self.repo / "objects").iterdir() if o.name.startswith(oid_prefix))
        commit = json.loads(self._load(oid))
        for p in self._tracked_files():
            p.unlink()
        for rel, blob in commit["tree"].items():
            (self.root / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.root / rel).write_bytes(self._load(blob))
        (self.repo / "HEAD").write_text(oid)
        print(f"Checked out {oid[:7]}: {commit['message']}")

def demo():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        git = MiniGit(root)
        git.init()
        (root / "hello.py").write_text("print('Hello')\n")
        first = git.commit("first commit")
        (root / "hello.py").write_text("print('Hello, World!')\nprint('Day 2')\n")
        (root / "notes.md").write_text("# Notes\n")
        print("\n📝 diff before the second commit:"); git.diff()
        git.commit("update greeting, add notes")
        git.commit("try an empty commit")
        print("\n📜 log:"); git.log()
        git.checkout(first[:7])
        print("hello.py is now:", (root / "hello.py").read_text().strip(), "| notes.md exists:", (root / "notes.md").exists())
        print("objects stored:", len(list((root / ".minigit" / "objects").iterdir())))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        g = MiniGit(".")
        cmd, *args = sys.argv[1:]
        {"init": g.init, "commit": lambda: g.commit(" ".join(args) or "no message"), "log": g.log,
         "diff": g.diff, "checkout": lambda: g.checkout(args[0])}[cmd]()
    else:
        demo()
