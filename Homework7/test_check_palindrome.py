from palindrome import check_palindrome
import unittest


class TestPalindromeCheck(unittest.TestCase):

    def test_palindrome_false(self):
        self.assertEqual(check_palindrome("123432"), False)

    def test_palindrome_true(self):
        self.assertEqual(check_palindrome("1234321"), True)

    def test_not_number(self):
        self.assertEqual(check_palindrome("123asa321"), None)
