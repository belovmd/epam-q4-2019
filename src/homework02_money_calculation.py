#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 02.2 Purchase money calculation
Sergey Streltsov 2019-10-22
"""


if __name__ == '__main__':
    dollars, cents = input('Enter a item price: dollars cents ').split()
    quantity = input('Enter a number of items: ')
    overall = (int(dollars) * 100 + int(cents)) * int(quantity)
    print('Total: {} dollars, {} cents'.format(overall // 100, overall % 100))
