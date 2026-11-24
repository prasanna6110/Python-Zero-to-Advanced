# Day 103 · subprocess: Running System Commands

_Advanced_

## subprocess
Runs other programs from Python.
```python
result = subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
result.stdout, result.stderr, result.returncode
```
## Key options
| Option | Meaning |
|--------|---------|
| `capture_output=True` | collect stdout and stderr |
| `text=True` | give back strings instead of bytes |
| `check=True` | raise `CalledProcessError` if the command fails |
| `timeout=5` | kill the command if it runs too long |
| `input="..."` | send data to its stdin |
| `cwd=`, `env=` | working directory and environment |

## ⚠️ Security
Pass a **list** of arguments. **Avoid `shell=True`** with user input, because it allows command injection. If you need shell-style splitting, use `shlex.split` and `shlex.quote`.

`subprocess.Popen` gives you streaming and more control.

## Examples

### Example 1: Running a command and capturing output  ([`example_1.py`](example_1.py))

```python
import subprocess, sys

result = subprocess.run([sys.executable, "-c", "print('hello from a child process')"],
                        capture_output=True, text=True)
print("stdout:", result.stdout.strip())
print("return code:", result.returncode)

r = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
print("version:", (r.stdout or r.stderr).strip())
```

### Example 2: Errors, timeouts and input  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Streaming output with Popen and safe quoting  ([`example_3.py`](example_3.py))

```python
import subprocess, sys, shlex

code = "import time\nfor i in range(3):\n    print('progress', i*50, '%', flush=True)\n    time.sleep(0.2)"
with subprocess.Popen([sys.executable, "-c", code], stdout=subprocess.PIPE, text=True) as proc:
    for line in proc.stdout:
        print("live >", line.strip())
print("exit:", proc.returncode)

user_input = "notes.txt; rm -rf /"
print("split :", shlex.split("grep -i 'hello world' file.txt"))
print("quoted:", "cat " + shlex.quote(user_input), "<- the injection is neutralised")
```

## Practice

1. Write a script that runs `git log --oneline -5` and parses the output.
2. Write a "ping" checker for a list of hosts (watch out for the OS-specific flags).
3. Pipe the output of one subprocess into another.

---

[⬅ Day 102](../Day-102-Working-with-Excel-PDF-and-Images-Popular-Libraries/README.md) · [🏠 Home](../README.md) · [Day 104 ➡](../Day-104-Security-Basics-hashing-secrets-and-hmac/README.md)
