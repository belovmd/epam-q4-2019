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


if __name__ == '__main__':
    five_divide(divider=5)
    five_divide()
    print_list_element(thelist=[1, 2, 3, 4, 5, 6], index=0)
    print_list_element(thelist=[1, 2, 3, 4, 5, 6], index=3)
    print_list_element(thelist=[1, 2, 3, 4, 5, 6], index=6)
