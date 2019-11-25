import unittest
import funcs


class Test_is_palindrome(unittest.TestCase):
    """Unit tests for funcs module."""

    def test_empty(self):
        self.assertEqual(funcs.is_palindrome(), True)

    def test_palindromes(self):
        self.assertTrue(funcs.is_palindrome(131))
        self.assertTrue(funcs.is_palindrome(12321))
        self.assertTrue(funcs.is_palindrome(11))
        self.assertTrue(funcs.is_palindrome(1))

    def test_not_palindromes(self):
        self.assertFalse(funcs.is_palindrome(1231))
        self.assertFalse(funcs.is_palindrome(123))
        self.assertFalse(funcs.is_palindrome(211))
        self.assertFalse(funcs.is_palindrome(12))


class Test_generate_numbers(unittest.TestCase):
    def test_default(self):
        self.assertEqual(len(funcs.generate_numbers().keys()), 20)

    def test_5(self):
        self.assertEqual(len(funcs.generate_numbers(5).keys()), 5)
        self.assertEqual(funcs.generate_numbers(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

    def test_1(self):
        self.assertEqual(len(funcs.generate_numbers(1).keys()), 1)
        self.assertEqual(funcs.generate_numbers(1), {1: 1, })


if __name__ == "__main__":
    unittest.main()
