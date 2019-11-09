#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 02.4 Task from another resources
Sergey Streltsov 2019-10-31

https://stepik.org/cert/206988 - my certificate for Automate
testing process with Selenium and Python

https://stepik.org/cert/25226 - my certificate for
Python, basics

https://www.codewars.com/users/Mantikor - Codewars profile

Register on https://stepik.org/catalog?language=en,
https://py.checkio.org/  site (or https://www.codewars.com,
https://www.hackerrank.com/, https://acmp.ru)
and solve 1-5 different tasks from Elementary (or any) level.
Add task description as a module docstring (at the top of the script).
"""

import sys


def letter_change():
    """In each word in the text change k-th letter to the
    selected symbol. If k > len(word) - exchange not needed.
    """

    input_text = input('Input text: ')
    position_index = input('Input index for change: ')
    position_index = int(position_index)
    if position_index <= 0:
        print('Error, need positive number!')
        return False
    symbol = input('Input symbol for change: ')
    if len(symbol) > 1:
        print('Error, need a one symbol!')
        return False
    text_list = input_text.split(' ')
    for word in text_list:
        if position_index <= len(word):
            word = word[:position_index - 1] + symbol + word[position_index:]
        print(word, end=' ')


def snowden():
    """The program should be executed by calling
    'python snowden.py cipheredmessage.txt' where "cipheredmessage.txt"
    is a file with a ciphered message sent by Bob.
    The message consists of lowercase English letters and its length
    is at most 100 000. Output the message after step
    2). The program should produce an answer in less than a few seconds.
    """
    
    if len(sys.argv) == 2:
        in_file = sys.argv[1]
    else:
        print('no valid file name...')
        sys.exit()

    test_str = open(in_file).read()
    test_list = [test_str[i] for i in range(len(test_str))]
    k = 0
    while k < (len(test_list) - 1):
        if test_list[k] == test_list[k + 1]:
            test_list.pop(k)
            test_list.pop(k)
            if k != 0:
                k -= 1
            continue
        else:
            k += 1
    res_str = ''.join(test_list)
    print(res_str)


if __name__ == '__main__':
    letter_change()
    snowden()
