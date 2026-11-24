# 065 · Unit Testing with unittest — Example 3: subTest for many inputs
# Run: python example_3.py

import unittest

def grade(marks):
    if marks >= 90: return "A"
    if marks >= 75: return "B"
    if marks >= 40: return "C"
    return "F"

class TestGrade(unittest.TestCase):
    def test_many(self):
        cases = [(95, "A"), (90, "A"), (80, "B"), (40, "C"), (10, "F")]
        for marks, expected in cases:
            with self.subTest(marks=marks):
                self.assertEqual(grade(marks), expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
