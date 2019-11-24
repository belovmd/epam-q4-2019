"""Create unit tests for any program from previous homeworks."""

from task import is_palindrome
import unittest


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome(123321))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome(12322))

    def test_exception(self):
        with self.assertRaises(ValueError):
            is_palindrome("12321")

    def test_negative(self):
        self.assertFalse(is_palindrome(-12321))
