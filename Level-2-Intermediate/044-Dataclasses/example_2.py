# 044 · Dataclasses — Example 2: Defaults, post_init and ordering
# Run: python example_2.py

from dataclasses import dataclass, field

@dataclass(order=True)
class Task:
    priority: int
    title: str = field(compare=False)
    tags: list = field(default_factory=list, compare=False)

    def __post_init__(self):
        if self.priority < 0:
            raise ValueError("priority must be >= 0")
        self.title = self.title.strip().title()

tasks = [Task(3, " write report "), Task(1, "fix bug", ["urgent"]), Task(2, "review pr")]
for t in sorted(tasks):
    print(t)
