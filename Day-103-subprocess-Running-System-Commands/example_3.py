# Day 103 · subprocess: Running System Commands — Streaming output with Popen and safe quoting
# Run: python example_3.py

import subprocess, sys, shlex

code = "import time\nfor i in range(3):\n    print('progress', i*50, '%', flush=True)\n    time.sleep(0.2)"
with subprocess.Popen([sys.executable, "-c", code], stdout=subprocess.PIPE, text=True) as proc:
    for line in proc.stdout:
        print("live >", line.strip())
print("exit:", proc.returncode)

user_input = "notes.txt; rm -rf /"
print("split :", shlex.split("grep -i 'hello world' file.txt"))
print("quoted:", "cat " + shlex.quote(user_input), "<- the injection is neutralised")
