from runner import runner
import unittest


class TestRunner(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(runner("is_palindrome"), [False])

    def test_generate_numbers(self):
        self.assertEqual(runner("generate_numbers"),
                         [{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}])

    def test_count_characters(self):
        self.assertEqual(runner("count_characters"),
                         [{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1}])

    def test_fizzbuzz(self):
        self.assertEqual(runner("fizzbuzz"),
                         [[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz']])

    def test_two(self):
        self.assertEqual(runner("is_palindrome", "fizzbuzz"),
                         [False,
                          [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz']])

    def test_default(self):
        self.assertEqual(runner(),
                         [{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1},
                          [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz'],
                          {1: 1, 2: 4, 3: 9, 4: 16, 5: 25},
                          False])

    def test_not_member(self):
        self.assertEqual(runner("is_pal"), [])

    def test_not_function(self):
        self.assertEqual(runner("variable"), [])

    def test_class(self):
        self.assertEqual(runner("SomeClass"), [])


if __name__ == '__main__':
    unittest.main()
