# Day 103 · subprocess: Running System Commands — Errors, timeouts and input
# Run: python example_2.py

import subprocess, sys

try:
    subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"], check=True)
except subprocess.CalledProcessError as e:
    print("Command failed with code", e.returncode)

try:
    subprocess.run([sys.executable, "-c", "import time; time.sleep(5)"], timeout=0.5)
except subprocess.TimeoutExpired:
    print("Command timed out")

r = subprocess.run([sys.executable, "-c", "import sys; print(sys.stdin.read().upper())"],
                   input="send this via stdin", capture_output=True, text=True)
print(r.stdout.strip())
