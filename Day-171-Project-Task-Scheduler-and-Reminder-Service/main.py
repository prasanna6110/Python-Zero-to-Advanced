# Day 171 · Project: Task Scheduler and Reminder Service — Task Scheduler
# Run: python main.py

import heapq
import itertools
import threading
import time
from datetime import datetime

class Scheduler:
    def __init__(self):
        self._jobs, self._lock = [], threading.Lock()
        self._wakeup, self._stop = threading.Event(), threading.Event()
        self._ids = itertools.count(1)
        self.log = []
        self._thread = threading.Thread(target=self._run, daemon=True)

    def every(self, seconds, times=None):
        def decorator(func):
            self.schedule(func, delay=seconds, interval=seconds, times=times)
            return func
        return decorator

    def schedule(self, func, delay=0.0, interval=None, times=None, args=()):
        with self._lock:
            jid = next(self._ids)
            heapq.heappush(self._jobs, (time.monotonic() + delay, jid, func, interval, times, args))
        self._wakeup.set()
        return jid

    def _run(self):
        while not self._stop.is_set():
            with self._lock:
                job = self._jobs[0] if self._jobs else None
            if job is None:
                self._wakeup.wait(); self._wakeup.clear(); continue
            when, jid, func, interval, times, args = job
            wait = when - time.monotonic()
            if wait > 0:
                self._wakeup.wait(wait); self._wakeup.clear(); continue
            with self._lock:
                heapq.heappop(self._jobs)
                if interval and (times is None or times > 1):
                    heapq.heappush(self._jobs, (when + interval, jid, func, interval,
                                                None if times is None else times - 1, args))
            try:
                result = func(*args)
                self.log.append((datetime.now().strftime("%H:%M:%S.%f")[:-3], func.__name__, "ok", result))
            except Exception as e:
                self.log.append((datetime.now().strftime("%H:%M:%S.%f")[:-3], func.__name__, "error", str(e)))

    def start(self):
        self._thread.start(); return self

    def stop(self):
        self._stop.set(); self._wakeup.set(); self._thread.join()

scheduler = Scheduler()

@scheduler.every(0.3, times=4)
def drink_water():
    print("💧 Reminder: drink water")

@scheduler.every(0.5, times=2)
def backup():
    print("💾 Backing up notes...")
    return "3 files"

def remind(msg):
    print(f"⏰ {msg}")

def flaky():
    raise ConnectionError("server down")

if __name__ == "__main__":
    scheduler.start()
    scheduler.schedule(remind, delay=0.2, args=("Micro-Grids class in 10 minutes",))
    scheduler.schedule(remind, delay=0.9, args=("Push today's code to GitHub",))
    scheduler.schedule(flaky, delay=0.4)
    time.sleep(1.5)
    scheduler.stop()
    print("\n📋 Run log:")
    for row in scheduler.log:
        print("  ", *row)
