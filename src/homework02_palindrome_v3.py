#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 02.1 Finding palindrome v3
Sergey Streltsov 2019-10-24

Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition.
"""


if __name__ == '__main__':
    input_str = input('Enter a number: ')
    try:
        num_value = value_copy = int(input_str)
        new_value = 0
        while num_value:
            remain = num_value % 10
            new_value = new_value * 10 + remain
            num_value //= 10
        print('Is palindrome: {}'.format(value_copy == new_value))
    except ValueError:
        print('Error, not a number')
