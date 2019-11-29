from first.task3 import add_to_list_in_dict
import unittest


class TestTask3(unittest.TestCase):

    def test_add_element_to_list(self):
        test_dict = {'one': [1, 2, 3], 'two': [1, 2, 3]}
        add_to_list_in_dict(thedict=test_dict, listname='one', element=4)
        self.assertEqual(test_dict, {'one': [1, 2, 3, 4], 'two': [1, 2, 3]})

    def test_add_key_and_element_to_dict(self):
        test_dict = {}
        add_to_list_in_dict(thedict=test_dict, listname='one', element=4)
        self.assertEqual(test_dict, {'one': [4]})

    def test_add_key_and_element_to_dict2(self):
        test_dict = {'one': [1, 2, 3]}
        add_to_list_in_dict(thedict=test_dict, listname='three', element=5)
        self.assertEqual(test_dict, {'one': [1, 2, 3], 'three': [5]})
