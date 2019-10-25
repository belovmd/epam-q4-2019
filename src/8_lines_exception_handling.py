#!/usr/bin/env python3.7

"""This program adds up integers from command line.

This program adds up integers that have been passed as
arguments in the command line.
8 lines: Command line arguments, exception handling
from https://wiki.python.org/moin/SimplePrograms .

"""

import sys
try:
    TOTAL = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', TOTAL)
except ValueError:
    print('Please supply integer arguments')
