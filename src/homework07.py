#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 07
Sergey Streltsov 2019-11-20
"""


def five_divide(divider=0):
    try:
        print('5/{}={}'.format(divider, 5 / divider))
    except ZeroDivisionError as e:
        print('Error: {}'.format(e))


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as e:
        print('Error: {}'.format(e))


def add_to_list_in_dict(thedict, listname, element):
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
