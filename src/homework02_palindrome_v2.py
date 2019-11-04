#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 02.1 Finding palindrome v2
Sergey Streltsov 2019-10-24

Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition.
"""

import math


def reverse_number(num):
    return num != 0 and ((num % 10) * (10 ** int(math.log(num, 10))) +
                         reverse_number(num // 10))


if __name__ == '__main__':
    input_str = input('Enter a number: ')
    try:
        num_value = int(input_str)
        print('Is palindrome: {}'.format(
            num_value == reverse_number(num_value)))
    except ValueError:
        print('Error, not a number')
