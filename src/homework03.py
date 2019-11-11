#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 03
Sergey Streltsov 2019-11-09
"""


def list_practice():
    """List practice

    Use a list comprehension to construct the list ['ab', 'ac', 'ad', 'bb',
    'bc', 'bd'].
    Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
    Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
    Simultaneously remove the element '2a' from the above list and print it.
    Copy the above list and add '2a' back into the list such that the
    original is still missing it.
    """
    src_lst = [i + j for i in 'ab' for j in 'bcd']
    print(src_lst)
    new_lst = src_lst[::2]
    print(new_lst)
    sec_lst = [ch + 'a' for ch in '1234']
    print(sec_lst)
    print('{} deleted'.format(sec_lst.pop(1)))
    thr_lst = sec_lst.copy()
    thr_lst.insert(1, '2a')
    print(thr_lst)


def tuple_practice():
    """Tuple practice

    Create the list ['a', 'b', 'c'], then create a tuple from that list.
    Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
    (Hint: the material needed to do this has been covered, but it's not
    entirely obvious)
    Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
    (That is, in one line of code).
    Create a tuple containing just a single element which in turn contains the
    three elements 'a', 'b', and 'c'. Verify that the length is actually 1 by
    using the len() function.
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

    Define a function generate_numbers(number) which returns a dictionary
    where the keys are numbers between 1 and n (both included) and the values
    are square of keys. n – function argument. Default is 20.
    """
    return {n: n * n for n in range(1, number + 1)}


def count_characters(count_me_string):
    """Dictionary practice

    Define a function count_characters(count_me_string) which count and return
    the numbers of each character in a count_me_string argument.
    """
    counted = dict()
    for ch in count_me_string:
        counted[ch] = counted.get(ch, 0) + 1
    return counted


if __name__ == '__main__':
    list_practice()
    tuple_practice()
    print(generate_numbers())
    test_str = input('Input string: ')
    print(count_characters(count_me_string=test_str))
