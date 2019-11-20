#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 07
Sergey Streltsov 2019-11-20
"""

import unittest


class TestAddToList(unittest.TestCase):
    def test_list_present(self):
        t_dict = dict()
        add_to_list_in_dict(thedict=t_dict, listname='2', element=2)
        self.assertDictEqual(t_dict, {'2': [2]}, 'Error')

    def test_no_list(self):
        t_dict = dict()
        add_to_list_in_dict(thedict=t_dict, listname='2', element=2)
        self.assertNotEqual(t_dict, {}, 'Error')

    def test_list_present(self):
        t_dict = {'one': [1, 2]}
        add_to_list_in_dict(thedict=t_dict, listname='one', element=3)
        self.assertDictEqual(t_dict, {'one': [1, 2, 3]}, 'Error')

    def test_add_same_element(self):
        t_dict = {'one': [1, 2]}
        add_to_list_in_dict(thedict=t_dict, listname='one', element=1)
        self.assertDictEqual(t_dict, {'one': [1, 2, 1]}, 'Error')

    def test_add_new_list(self):
        t_dict = {'one': [1, 2]}
        add_to_list_in_dict(thedict=t_dict, listname='two', element=99)
        self.assertDictEqual(t_dict, {'one': [1, 2], 'two': [99]}, 'Error')

    def test_palindrome_true(self):
        p = is_palindrome(input_str='12321')
        self.assertEqual(p, True, 'Error')

    def test_palindrome_false(self):
        p = is_palindrome(input_str='123456')
        self.assertEqual(p, False, 'Error')

    def test_palindrome_not_num(self):
        p = is_palindrome(input_str='abcd')
        self.assertEqual(p, -1, 'Error')

    @unittest.skip('skipping this test')
    def test_test_for_skip(self):
        p = is_palindrome(input_str=567)
        self.assertEqual(p, False, 'Error')


def is_palindrome(input_str='7890987'):
    """EPAM python q4 homework 07.2

    Write a program that check whether a number is palindrome or Not.
    Input string contains only numbers.
    Please work only arithmetic operations, loops and if-condition.
    """
    if not input_str:
        input_str = input('Enter a number: ')
    try:
        num_value = value_copy = int(input_str)
        new_value = 0
        while num_value:
            remain = num_value % 10
            new_value = new_value * 10 + remain
            num_value //= 10
        return value_copy == new_value
    except ValueError:
        print('Error, not a number')
        return -1


def five_divide(divider=0):
    """EPAM python q4 homework 07.1.1

    Write a function to compute 5/0 and use try/except to catch
    the DivisionError exception.
    """
    try:
        print('5/{}={}'.format(divider, 5 / divider))
    except ZeroDivisionError as e:
        print('Error: {}'.format(e))


def print_list_element(thelist, index):
    """EPAM python q4 homework 07.1.2

    Add a try-except statement to the body of this function which handles
    a possible IndexError, which could occur if the index provided exceeds
    the length of the list. Print an error message if this happens.
    """
    try:
        print(thelist[index])
    except IndexError as e:
        print('Error: {}'.format(e))


def add_to_list_in_dict(thedict, listname, element):
    """EPAM python q4 homework 07.1.3

    This function adds an element to a list inside a dict of lists.
    Rewrite it to use a try-except statement which handles a possible
    KeyError if the list with the name provided doesn’t exist in the
    dictionary yet, instead of checking beforehand whether it does.
    Include else and finally clauses in your try-except block.
    """
    try:
        l = thedict[listname]
    except KeyError as e:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(l)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


if __name__ == '__main__':
    five_divide(divider=5)
    five_divide()
    print_list_element(thelist=[1, 2, 3, 4, 5, 6], index=0)
    print_list_element(thelist=[1, 2, 3, 4, 5, 6], index=3)
    print_list_element(thelist=[1, 2, 3, 4, 5, 6], index=6)
    test_dict = {'one': [1, 2, 3, 4], 'two': [5, 6, 7, 8], 'three': [9, 10]}
    add_to_list_in_dict(thedict=test_dict, listname='one', element=5)
    add_to_list_in_dict(thedict=test_dict, listname='four', element=444)
    unittest.main()
