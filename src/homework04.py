#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 04
Sergey Streltsov 2019-11-12
"""


import math
import time


alternatively_history = []


def save_history(f_name):
    """History decorator

    Create a decorator that stores the results of function calls and the
    time it takes to get the result during program startup
    """
    history = list()
    global alternatively_history

    def wrapper(*args, **kwargs):
        start_time = time.time()
        f_result = f_name(*args, **kwargs)
        stop_time = time.time()
        est_time_msec = (int(stop_time - start_time) * 1000)
        history.append({'name': f_name.__name__,
                        'result': f_result,
                        'time_ms': est_time_msec})
        alternatively_history.append({'name': f_name.__name__,
                                      'result': f_result,
                                      'time_ms': est_time_msec})
        return f_result
    return wrapper


@save_history
def count_factorial(x):
    return math.factorial(x)


def get_ranges(in_list):
    """Collapsed list

    Implement the get_ranges function which receives a non-empty list
    of non-repeating integers, sorted in ascending order, which this
    list “collapses”
    """
    last = None
    raw_str = ''
    for number in in_list:
        if not (last is None):
            if number - last == 1:
                raw_str += ('-' + str(number))
                last = number
            else:
                raw_str += ',' + str(number)
                last = number
        else:
            raw_str += str(number)
            last = number
    new_list = list()
    for block in raw_str.split(','):
        if block.count('-') > 1:
            new_block = '-'.join([block.split('-')[0], block.split('-')[-1]])
        else:
            new_block = block
        new_list.append(new_block)
    new_str = ','.join(new_list)
    return new_str


def get_ranges_v2(in_list):
    """Collapsed list v2

    Implement the get_ranges function which receives a non-empty list
    of non-repeating integers, sorted in ascending order, which this
    list “collapses”
    """
    out_str = ''
    for n in range(len(in_list) - 1):
        if in_list[n] != in_list[n + 1] - 1:
            out_str += str(in_list[n]) + ','
        elif in_list[n] != in_list[n - 1] + 1 or not n:
            out_str += str(in_list[n]) + '-'
    return out_str + str(in_list[-1])


if __name__ == '__main__':
    for i in range(9000, 9005):
        fact = count_factorial(i)
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4, 7, 10]))
    print(get_ranges([2, 3, 8, 9]))
    print(get_ranges([100]))
    print(get_ranges_v2([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges_v2([4, 7, 10]))
    print(get_ranges_v2([2, 3, 8, 9]))
    print(get_ranges_v2([100]))
