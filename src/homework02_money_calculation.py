#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 02.2 Purchase money calculation
Sergey Streltsov 2019-10-22

Write a program to calculate total cost. One item costs M dollars and N cents.
Customer bought L items. Print total price in dollars and cents for L items.
For example
Input data:  one item price is 3 dollars 20 cents, calculate price for 3 items
Output data: Total cost:  9 dollars 60 cents.
"""


if __name__ == '__main__':
    dollars, cents = input('Enter a item price: dollars cents ').split()
    quantity = input('Enter a number of items: ')
    overall = (int(dollars) * 100 + int(cents)) * int(quantity)
    print('Total: {} dollars, {} cents'.format(overall // 100, overall % 100))
