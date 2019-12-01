from HW7_task1_3 import add_to_list_in_dict as add_to_lst
import HWs2_5
import runner
import sys
import unittest
if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch


class TestHomework7AddToListInDict(unittest.TestCase):
    def test_add_to_new_list(self):
        self.assertEqual(add_to_lst({'key1': [1, 2], 'key2': [4]}, 'new_k', 8),
                         {'key1': [1, 2], 'key2': [4], 'new_k': [8]})

    def test_add_to_old_list(self):
        self.assertEqual(add_to_lst({'key1': [1, 2], 'key2': [4]}, 'key2', 5),
                         {'key1': [1, 2], 'key2': [4, 5]})

    def test_error_if_not_dict_argument(self):
        with self.assertRaises(Exception):
            add_to_lst({'key1', 'key2'}, 'key2', 7)


class TestCountMeString(unittest.TestCase):
    def test_character_with_count__more_than_1(self):
        with patch('builtins.input', return_value="abcdefbbc"):
            self.assertEqual(HWs2_5.count_characters(),
                             {'a': 1, 'b': 3, 'c': 2, 'd': 1, 'e': 1, 'f': 1})

    def test_string_with_one_character(self):
        with patch('builtins.input', return_value="a"):
            self.assertEqual(HWs2_5.count_characters(), {'a': 1})

    def test_empty_input(self):
        with patch('builtins.input', return_value=""):
            self.assertEqual(HWs2_5.count_characters(), {})


class TestFindingPalindrome(unittest.TestCase):
    def test_some_not_palindrome(self):
        with patch('builtins.input', return_value='45242'):
            self.assertFalse(HWs2_5.finding_palindrome())

    def test_some_palindrome(self):
        with patch('builtins.input', return_value='1145665411'):
            self.assertTrue(HWs2_5.finding_palindrome())

    def test_one_numeral_palindrome(self):
        with patch('builtins.input', return_value='7'):
            self.assertTrue(HWs2_5.finding_palindrome())

    def test_two_numeral_palindrome(self):
        with patch('builtins.input', return_value='11'):
            self.assertTrue(HWs2_5.finding_palindrome())

    def test_error_if_input_is_empty(self):
        with patch('builtins.input', return_value=''):
            with self.assertRaises(Exception):
                HWs2_5.finding_palindrome()

    def test_error_if_input_not_number(self):
        with patch('builtins.input', return_value='text'):
            with self.assertRaises(Exception):
                HWs2_5.finding_palindrome()


class TestFizzBuzz(unittest.TestCase):
    def test_whole_answer(self):
        self.assertEqual(HWs2_5.fizzbuzz(),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
                          'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17,
                          'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz',
                          26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34,
                          'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz',
                          43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz',
                          'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59,
                          'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67,
                          68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz',
                          76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz',
                          'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92,
                          'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']
                         )


class TestGenerateNumbers(unittest.TestCase):
    def test_default_arg(self):
        self.assertEqual(HWs2_5.generate_numbers(),
                         {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,
                          9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196,
                          15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400
                          })

    def test_not_default_arg(self):
        self.assertEqual(HWs2_5.generate_numbers(13),
                         {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,
                          9: 81, 10: 100, 11: 121, 12: 144, 13: 169})

    def test_error_if_not_int_argument(self):
        with self.assertRaises(Exception):
            HWs2_5.generate_numbers('twenty')


class TestRunner(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(runner.runner('fizzbuzz'),
                         [[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
                           'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17,
                           'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz',
                           26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34,
                           'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz',
                           43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz',
                           'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59,
                           'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67,
                           68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz',
                           76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz',
                           'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92,
                           'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']]
                         )

    def test_generate_numbers(self):
        self.assertEqual(runner.runner('generate_numbers'),
                         [{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,
                           9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196,
                           15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400
                           }])

    def test_two_functions_together(self):
        self.assertEqual(runner.runner('fizzbuzz', 'generate_numbers'),
                         [[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
                           'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17,
                           'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz',
                           26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34,
                           'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz',
                           43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz',
                           'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59,
                           'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67,
                           68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz',
                           76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz',
                           'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92,
                           'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz'],
                          {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,
                           9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196,
                           15: 225, 16: 256, 17: 289, 18: 324, 19: 361,
                           20: 400}
                          ])

    @patch('HWs2_5.finding_palindrome')
    @patch('HWs2_5.count_characters')
    def test_runner_without_args(self, mocked_count_char, mocked_find_palindr):
        runner.runner()
        assert mocked_count_char.called
        assert mocked_find_palindr.called


if __name__ == '__main__':
    unittest.main()
