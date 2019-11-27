"""Cover function from 1.3 with tests."""
from task1_3 import add_to_list_in_dict
import unittest


class FuncTest(unittest.TestCase):
    def test_if_exists(self):
        self.dct = {'a': [1, 2], 'b': ['sx', 12]}
        self.res = add_to_list_in_dict(self.dct, 'a', 'df')
        self.assertEqual(self.res, self.dct)

    def test_if_not_exists(self):
        self.dct = {'a': [1], 'b': [2]}
        self.res = add_to_list_in_dict(self.dct, 'c', 3)
        self.assertEqual(self.res, self.dct)


if __name__ == '__main__':
    unittest.main()
