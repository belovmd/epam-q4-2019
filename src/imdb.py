#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 05 2
Sergey Streltsov 2019-11-17
"""


import os
import sys


def load_ratings(filename):
    run_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(run_path, filename)
    if os.path.isfile(full_path):
        with open(full_path, 'r') as settings_file:
            try:
                result = ''
            except:
                sys.exit('Error: loading file {}'.format(full_path))
    else:
        sys.exit('Error: No file {} found'.format(full_path))
    return result, run_path


if __name__ == '__main__':
    ratings, f_path = load_ratings('ratings.list')
