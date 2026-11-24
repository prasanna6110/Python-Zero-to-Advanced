# Day 052 · Enums — Basic Enum
# Run: python example_1.py

from enum import Enum

class Status(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

order_status = Status.SHIPPED
print(order_status, order_status.name, order_status.value)
print(Status("delivered"), Status["PENDING"])
for s in Status:
    print(" -", s.name)
print(order_status == Status.SHIPPED, order_status is Status.SHIPPED)
