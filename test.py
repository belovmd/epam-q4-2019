from palindrome import palindrome
import unittest


class TestMetods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(palindrome(123), False)

    def test_2(self):
        self.assertEqual(palindrome(12321), True)
