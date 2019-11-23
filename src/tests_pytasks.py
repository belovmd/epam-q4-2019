""" Tests for pytasks.py """

import pytasks
import unittest


class TestPytasks(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(pytasks.palindrome(), True)
        self.assertEqual(pytasks.palindrome(123), False)
        self.assertEqual(pytasks.palindrome('sas'), 'Input must be a number')

    def test_get_numbers(self):
        self.assertEqual(pytasks.gen_numbers(), {1: 1, 2: 4, 3: 9})
        self.assertEqual(pytasks.gen_numbers(5),
                         {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

    def test_fizz_buzz(self):
        self.assertEqual(pytasks.fizzbuzz(), [1, 2])
        self.assertEqual(pytasks.fizzbuzz(5), [1, 2, 'Fizz', 4, 'Buzz'])


if __name__ == '__main__':
    unittest.main()
