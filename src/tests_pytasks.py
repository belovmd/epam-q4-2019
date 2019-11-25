""" Tests for pytasks.py """

import pytasks
import unittest


class TestPalindrome(unittest.TestCase):
    def test_default_value(self):
        self.assertEqual(pytasks.palindrome(), True)

    def test_number(self):
        self.assertEqual(pytasks.palindrome(123), False)

    def test_str(self):
        self.assertEqual(pytasks.palindrome('sas'), 'Input must be a number')


class TestGetNumbers(unittest.TestCase):
    def test_default_value(self):
        self.assertEqual(pytasks.gen_numbers(), {1: 1, 2: 4, 3: 9})

    def test_input_value(self):
        self.assertEqual(pytasks.gen_numbers(5),
                         {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})


class TestFizzBuzz(unittest.TestCase):
    def test_default_value(self):
        self.assertEqual(pytasks.fizzbuzz(), [1, 2])

    def test_input_value(self):
        self.assertEqual(pytasks.fizzbuzz(5), [1, 2, 'Fizz', 4, 'Buzz'])


if __name__ == '__main__':
    unittest.main()
