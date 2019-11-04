#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 02.1 Finding palindrome
Sergey Streltsov 2019-10-22

Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition.
"""


if __name__ == '__main__':
    word = input('Enter a word: ')
    codes_list = [ord(i) for i in word]
    is_palindrome = 0
    cl_length = len(codes_list)
    if len(codes_list) % 2 != 0:
        del(codes_list[cl_length // 2])
    for i in range(cl_length // 2):
        is_palindrome += (codes_list[i] - codes_list[-(i + 1)])
    print(not is_palindrome)
