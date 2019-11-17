#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 05 1
Sergey Streltsov 2019-11-17
runner for functions from pytasks module
"""


import pytasks
import sys


def runner(args):
    """Functions runner

    Run functions from pytasks module, can be imported
    or use as command line script
    in command line you can specify function names
    for call, like as runner.py fizzbuzz is_palindrome
    """
    if not args:
        args = [func for func in dir(pytasks) if not func.startswith("__")]
    [print(getattr(pytasks, func)()) for func in args]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        runner(sys.argv[1:])
    else:
        runner(args=None)
