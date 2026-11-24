# Day 054 · Generators and yield — A generator pipeline
# Run: python example_3.py

log_lines = [
    "INFO user login",
    "ERROR disk full",
    "INFO page view",
    "ERROR timeout db",
    "WARN slow query",
]

def read(lines):
    for line in lines:
        yield line

def only_errors(lines):
    for line in lines:
        if line.startswith("ERROR"):
            yield line

def messages(lines):
    for line in lines:
        yield line.split(" ", 1)[1].upper()

pipeline = messages(only_errors(read(log_lines)))
for msg in pipeline:
    print(msg)

def chain_all(*iterables):
    for it in iterables:
        yield from it
print(list(chain_all([1, 2], "ab", range(3))))
