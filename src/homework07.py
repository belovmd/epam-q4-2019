#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 07
Sergey Streltsov 2019-11-20
"""

import hashlib


def five_divide(divider=0):
    try:
        print('5/{}={}'.format(divider, 5 / divider))
    except ZeroDivisionError as e:
        print('Error: {}'.format(e))


if __name__ == '__main__':
    five_divide(divider=5)
    five_divide()
