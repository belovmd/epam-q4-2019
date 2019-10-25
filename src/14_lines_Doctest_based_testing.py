#!/usr/bin/env python3.7

"""Doctest-based testing.

14 lines: Doctest-based testing from
https://wiki.python.org/moin/SimplePrograms .

"""


def median(pool):
    """Statistical median to demonstrate doctest.

    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    6 #change to 7 in order to pass the test
    """
    copy = sorted(pool)
    size = len(copy)
    return copy[int((size - 1) / 2)] if size % 2 == 1  \
        else (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2


if __name__ == '14_lines_Doctest_based_testing':
    import doctest
    doctest.testmod()
