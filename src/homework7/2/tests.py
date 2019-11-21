from runner import runner
import unittest


class TestRunner(unittest.TestCase):
    def test_run(self):
        self.assertEqual(runner("is_palindrome"), [False])
        self.assertEqual(runner("fizzbuzz"),
                         [[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz']])
        self.assertEqual(runner("generate_numbers"),
                         [{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}])
        self.assertEqual(runner("count_characters"),
                         [{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1}])
        self.assertEqual(runner("is_palindrome", "fizzbuzz"),
                         [False,
                          [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz']])

    def test_default_run(self):
        self.assertEqual(runner(),
                         [{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1},
                          [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz'],
                          {1: 1, 2: 4, 3: 9, 4: 16, 5: 25},
                          False])

    def test_run_not_member(self):
        self.assertEqual(runner("is_pal"), [])

    def test_run_not_function(self):
        self.assertEqual(runner("variable"), [])

    def test_run_class(self):
        self.assertEqual(runner("SomeClass"), [])


if __name__ == '__main__':
    unittest.main()
