# 090 · subprocess: Running System Commands — Example 1: Running a command and capturing output
# Run: python example_1.py

import subprocess, sys

result = subprocess.run([sys.executable, "-c", "print('hello from a child process')"],
                        capture_output=True, text=True)
print("stdout:", result.stdout.strip())
print("return code:", result.returncode)

r = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
print("version:", (r.stdout or r.stderr).strip())
