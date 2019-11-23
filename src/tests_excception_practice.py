""" Tests for exception.py """
from exception_practice import add_to_list_in_dict
from exception_practice import division
from exception_practice import print_list_element
import unittest


class TestExceptionPractice(unittest.TestCase):
    def setUp(self):
        self.dict_ = {'digits': [1]}

    def test_without_key_error(self):
        self.assertEqual(add_to_list_in_dict(self.dict_, 'digits', 1),
                         {'digits': [1, 1]})

    def test_with_key_error(self):
        self.assertEqual(add_to_list_in_dict(self.dict_, 'digit', 1),
                         {'digits': [1], 'digit': [1]})


class TestPrintListElement(unittest.TestCase):
    def setUp(self):
        self.list_ = [1, 2, 3]

    def test_without_index_error(self):
        self.assertEqual(print_list_element(self.list_, 0), 1)

    def test_with_index_error(self):
        self.assertEqual(print_list_element(self.list_, 20),
                         "list index out of range")


class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(10, 2), 5.0)
        self.assertEqual(division(5, 0), "division by zero")


if __name__ == '__main__':
    unittest.main()
