from Homework7 import add_to_list_in_dict
from Homework7 import dict1
import unittest


class TestFunction(unittest.TestCase):

    def test1(self):
        add_to_list_in_dict(dict1, 2, 3)
        self.assertEqual(dict1, {1: [556], 2: [3]})

    def test2(self):
        add_to_list_in_dict(dict1, 1, 3)
        self.assertEqual(dict1, {1: [556, 3]})


if __name__ == "__main__":
    unittest.main()
