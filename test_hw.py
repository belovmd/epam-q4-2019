from HW7_task1_3 import add_to_list_in_dict as add_to_lst
import HWs2_5
import sys
import unittest
if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch


class TestHomework7Task1part3(unittest.TestCase):
    def test_add_to_list_in_dict(self):
        ex_dict = {'key1': [1, 2, 3], 'key2': [4]}
        self.assertEqual(add_to_lst(ex_dict, 'new_key', 77)['new_key'], [77])
        self.assertEqual(add_to_lst(ex_dict, 'new_key', 77)['key1'], [1, 2, 3])
        self.assertEqual(add_to_lst(ex_dict, 'key2', 5)['key2'], [4,5])


class TestPreviousHomeworks(unittest.TestCase):
    def test_count_me_string(self):
        with patch('builtins.input', return_value="abcdefbbc"):
            self.assertEqual(HWs2_5.count_characters()['b'], 3)
        with patch('builtins.input', return_value="abcdefbbc"):
            self.assertEqual(HWs2_5.count_characters()['a'], 1)

    def test_finding_palindrome(self):
        with unittest.mock.patch('builtins.input', return_value=45242):
            self.assertFalse(HWs2_5.finding_palindrome())
        with unittest.mock.patch('builtins.input', return_value=1145665411):
            self.assertTrue(HWs2_5.finding_palindrome())
        with unittest.mock.patch('builtins.input', return_value=7):
            self.assertTrue(HWs2_5.finding_palindrome())
        with unittest.mock.patch('builtins.input', return_value=11):
            self.assertTrue(HWs2_5.finding_palindrome())
        with unittest.mock.patch('builtins.input', return_value='11'):
            self.assertTrue(HWs2_5.finding_palindrome())

    def test_fizzbuzz(self):
        self.assertEqual(HWs2_5.fizzbuzz()[1], 2)
        self.assertEqual(HWs2_5.fizzbuzz()[14], 'FizzBuzz')
        self.assertEqual(HWs2_5.fizzbuzz()[17], 'Fizz')
        self.assertEqual(HWs2_5.fizzbuzz()[84], 'Buzz')
        self.assertEqual(HWs2_5.fizzbuzz()[99], 'Buzz')

    def test_generate_numbers(self):
        self.assertEqual(HWs2_5.generate_numbers()[1], 1)
        self.assertEqual(HWs2_5.generate_numbers()[20], 400)
        self.assertEqual(HWs2_5.generate_numbers(100)[100], 10000)


if __name__ == '__main__':
    unittest.main()
