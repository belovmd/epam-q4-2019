"""Cover function from 1.3 with tests."""
from task1_3 import add_to_list_in_dict
import unittest


class FuncTest(unittest.TestCase):
    def setUp(self):
        self.dct = {'a': [1, 2], 'b': ['sx', 12]}
        self.dct1 = {'a': [1], 'b': [2]}
        self.res = add_to_list_in_dict(self.dct, 'a', 'df')
        self.res1 = add_to_list_in_dict(self.dct1, 'c', 3)

    def test_exixts(self):
        self.assertEqual(self.res, {'a': [1, 2, 'df'], 'b': ['sx', 12]})

    def test_not_exists(self):
        self.assertEqual(self.res1, {'a': [1], 'b': [2], 'c': [3]})


if __name__ == '__main__':
    unittest.main()
