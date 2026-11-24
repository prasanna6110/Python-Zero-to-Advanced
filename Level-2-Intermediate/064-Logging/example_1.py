# 064 · Logging — Example 1: Basic logging
# Run: python example_1.py

import logging, sys

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout,
                    format="%(levelname)-8s %(message)s")
logging.debug("Detailed info for debugging")
logging.info("Server started on port 8000")
logging.warning("Disk usage at 85%")
logging.error("Could not connect to database")
logging.critical("System is shutting down!")
