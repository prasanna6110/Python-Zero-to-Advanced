# Day 074 · Unit Testing with unittest — Testing simple functions
# Run: python example_1.py

import unittest

def is_palindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_palindrome("madam"))

    def test_sentence(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
