#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 03
Sergey Streltsov 2019-11-09
"""


def list_practice():
    """List practice
    """
    src_lst = [i + j for i in 'ab' for j in 'bcd']
    print(src_lst)
    new_lst = src_lst[::2]
    print(new_lst)
    sec_lst = [str(i) + 'a' for i in range(1, 5)]
    print(sec_lst)
    print('{} deleted'.format(sec_lst.pop(1)))
    thr_lst = sec_lst.copy()
    thr_lst.insert(1, '2a')
    print(thr_lst)


def tuple_practice():
    """Tuple practice
    """
    simple_lst = ['a', 'b', 'c']
    print(simple_lst)
    simple_tpl = tuple(simple_lst)
    print(simple_tpl)
    lst2 = list(simple_tpl)
    print(lst2)
    a, b, c = 'a', 2, 'gamma'
    print('a={}, b={}, c={}'.format(a, b, c))
    tpl2 = (('a', 'b', 'c'), )
    print('{}, length: {}'.format(tpl2, len(tpl2)))


def generate_numbers(number=20):
    """Dictionary practice
    """
    return {n: n * n for n in range(1, number + 1)}


def count_characters(count_me_string):
    """Dictionary practice 2
    """
    return {letter: count_me_string.count(letter) for letter in count_me_string}


if __name__ == '__main__':
    list_practice()
    tuple_practice()
    print(generate_numbers())
    test_str = input('Input string: ')
    print(count_characters(count_me_string=test_str))
