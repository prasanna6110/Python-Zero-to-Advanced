# Day 163 · Project: Async Web Crawler

_Projects_

**Concepts:** asyncio, a work queue with worker tasks, a semaphore to limit concurrency, retries with exponential backoff, URL joining.

It crawls a (simulated) website concurrently, handles flaky pages and reports the status of every page.

## Code

### Async Web Crawler  ([`main.py`](main.py))

```python
import asyncio, random, time
from urllib.parse import urljoin

random.seed(11)
FAKE_WEB = {
    "https://site.com/": ["/about", "/blog", "/shop"],
    "https://site.com/about": ["/team", "/"],
    "https://site.com/blog": ["/blog/python", "/blog/asyncio", "/broken"],
    "https://site.com/shop": ["/shop/cart"],
    "https://site.com/team": [], "https://site.com/blog/python": ["/blog/asyncio"],
    "https://site.com/blog/asyncio": [], "https://site.com/shop/cart": [],
}

async def fetch(url):
    await asyncio.sleep(random.uniform(0.05, 0.2))
    if url.endswith("/broken"):
        raise ConnectionError("404")
    if random.random() < 0.2:
        raise TimeoutError("flaky network")
    return FAKE_WEB[url]

async def fetch_with_retry(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            return await fetch(url)
        except TimeoutError:
            await asyncio.sleep(0.05 * 2 ** attempt)          # exponential backoff
    raise TimeoutError(f"gave up on {url}")

async def crawl(start, max_concurrency=3, workers=4):
    queue, seen, results = asyncio.Queue(), {start}, {}
    sem = asyncio.Semaphore(max_concurrency)
    await queue.put(start)

    async def worker(name):
        while True:
            url = await queue.get()
            try:
                async with sem:
                    links = await fetch_with_retry(url)
                results[url] = f"ok ({len(links)} links)"
                for link in links:
                    full = urljoin(url, link)
                    if full not in seen:
                        seen.add(full); await queue.put(full)
            except Exception as e:
                results[url] = f"error: {e}"
            finally:
                queue.task_done()

    tasks = [asyncio.create_task(worker(f"w{i}")) for i in range(workers)]
    await queue.join()
    for t in tasks: t.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    return results

start = time.perf_counter()
report = asyncio.run(crawl("https://site.com/"))
for url, status in sorted(report.items()):
    print(f"{url:<32} {status}")
print(f"crawled {len(report)} pages in {time.perf_counter() - start:.2f}s")
```

## Extend this project

1. Use real `aiohttp` and respect `robots.txt`.
2. Save the link graph and draw it.
3. Add a depth limit and a domain filter.

---

[⬅ Day 162](../Day-162-Project-Key-Value-Database-Server-Mini-Redis/README.md) · [🏠 Home](../README.md) · [Day 164 ➡](../Day-164-Project-Mini-Web-Framework-like-Flask/README.md)
