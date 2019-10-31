#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 02.3 FizzBuzz
Sergey Streltsov 2019-10-22

Write a program that prints the numbers from 1 to 100,
but for multiples of three print “Fizz” instead of the number
and for multiples of five print “Buzz”.
For numbers which are multiples of both three and five, print “FizzBuzz”.
( http://en.wikipedia.org/wiki/Biz... )
"""


if __name__ == '__main__':
    for number in range(1, 101):
        if number % 15 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)
