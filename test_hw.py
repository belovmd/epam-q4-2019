from HW7_task1_3 import add_to_list_in_dict as add_to_lst
import HWs2_5
from runner import runner
import sys
import unittest
if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch


class TestHomework7AddToListInDict(unittest.TestCase):
    ex_dict = {'key1': [1, 2], 'key2': [4]}

    def test_new_list_after_add_to_new_list(self):
        self.assertEqual(add_to_lst(self.ex_dict, 'new_k', 8)['new_k'], [8])

    def test_old_list_after_add_to_new_list(self):
        self.assertEqual(add_to_lst(self.ex_dict, 'new_k', 8)['key1'], [1, 2])

    def test_after_add_to_old_list(self):
        self.assertEqual(add_to_lst(self.ex_dict, 'key2', 5)['key2'], [4, 5])

    def test_error_if_not_dict_argument(self):
        with self.assertRaises(Exception):
            add_to_lst({'key1', 'key2'}, 'key2', 7)


class TestCountMeString(unittest.TestCase):
    def test_character_with_count__more_than_1(self):
        with patch('builtins.input', return_value="abcdefbbc"):
            self.assertEqual(HWs2_5.count_characters()['b'], 3)

    def test_character_with_count_1(self):
        with patch('builtins.input', return_value="abcdefbbc"):
            self.assertEqual(HWs2_5.count_characters()['a'], 1)

    def test_string_with_one_character(self):
        with patch('builtins.input', return_value="abcdefbbc"):
            self.assertEqual(HWs2_5.count_characters()['a'], 1)

    def test_empty_input(self):
        with patch('builtins.input', return_value=""):
            self.assertEqual(HWs2_5.count_characters(), {})


class TestFindingPalindrome(unittest.TestCase):
    def test_some_not_palindrome(self):
        with unittest.mock.patch('builtins.input', return_value='45242'):
            self.assertFalse(HWs2_5.finding_palindrome())

    def test_some_palindrome(self):
        with unittest.mock.patch('builtins.input', return_value='1145665411'):
            self.assertTrue(HWs2_5.finding_palindrome())

    def test_one_numeral_palindrome(self):
        with unittest.mock.patch('builtins.input', return_value='7'):
            self.assertTrue(HWs2_5.finding_palindrome())

    def test_two_numeral_palindrome(self):
        with unittest.mock.patch('builtins.input', return_value='11'):
            self.assertTrue(HWs2_5.finding_palindrome())

    def test_error_if_input_is_empty(self):
        with unittest.mock.patch('builtins.input', return_value=''):
            with self.assertRaises(Exception):
                HWs2_5.finding_palindrome()

    def test_error_if_input_not_number(self):
        with unittest.mock.patch('builtins.input', return_value='text'):
            with self.assertRaises(Exception):
                HWs2_5.finding_palindrome()


class TestFizzBuzz(unittest.TestCase):
    def test_second_number(self):
        self.assertEqual(HWs2_5.fizzbuzz()[1], 2)

    def test_multiple_of_15(self):
        self.assertEqual(HWs2_5.fizzbuzz()[14], 'FizzBuzz')

    def test_multiple_of_3(self):
        self.assertEqual(HWs2_5.fizzbuzz()[17], 'Fizz')

    def test_multiple_of_5(self):
        self.assertEqual(HWs2_5.fizzbuzz()[84], 'Buzz')

    def test_last_number(self):
        self.assertEqual(HWs2_5.fizzbuzz()[99], 'Buzz')


class TestGenerateNumbers(unittest.TestCase):
    def test_number_1(self):
        self.assertEqual(HWs2_5.generate_numbers()[1], 1)

    def test_last_number(self):
        self.assertEqual(HWs2_5.generate_numbers()[20], 400)

    def test_last_number_if_not_default_length(self):
        self.assertEqual(HWs2_5.generate_numbers(100)[100], 10000)

    def func_for_exception(self):
        raise Exception('lets see if this works')

    def test_error_if_not_int_argument(self):
        with self.assertRaises(Exception):
            HWs2_5.generate_numbers('twenty')


class TestRunner(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(runner('fizzbuzz')[0][4], 'Buzz')

    def test_generate_numbers(self):
        self.assertEqual(runner('generate_numbers')[0][4], 16)

    def test_fizzbuzz_and_generate_numbers(self):
        self.assertEqual(runner('fizzbuzz', 'generate_numbers')[0][5], 'Fizz')
        self.assertEqual(runner('fizzbuzz', 'generate_numbers')[1][6], 36)


if __name__ == '__main__':
    unittest.main()
