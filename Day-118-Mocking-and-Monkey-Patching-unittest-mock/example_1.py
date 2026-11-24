# Day 118 · Mocking and Monkey Patching (unittest.mock) — Mock objects and side_effect
# Run: python example_1.py

from unittest.mock import Mock, MagicMock

payment = Mock()
payment.charge.return_value = {"status": "ok", "id": "txn_1"}
print(payment.charge(500, currency="INR"))
payment.charge.assert_called_once_with(500, currency="INR")
print("calls:", payment.charge.call_args_list)

flaky = Mock(side_effect=[ConnectionError("down"), "success"])
for _ in range(2):
    try:
        print(flaky())
    except ConnectionError as e:
        print("raised:", e)

m = MagicMock()
m.__len__.return_value = 3
m.__getitem__.side_effect = lambda k: k * 2
print(len(m), m[21])
