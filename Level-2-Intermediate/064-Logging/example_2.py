# 064 · Logging — Example 2: Named loggers, handlers and files
# Run: python example_2.py

import logging, sys, os

logger = logging.getLogger("payment")
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("[%(name)s] %(levelname)s: %(message)s"))
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(console)
logger.addHandler(file_handler)

logger.debug("only in the file")
logger.info("payment received")
file_handler.close()
print("--- app.log contents ---")
print(open("app.log").read().strip())
os.remove("app.log")
