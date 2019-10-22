#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 02.3 FizzBuzz
Sergey Streltsov 2019-10-22
"""


if __name__ == '__main__':
    for number in range(1, 101):
        if (number % 3 == 0) and (number % 5 == 0):
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)
