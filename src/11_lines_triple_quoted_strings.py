#!/usr/bin/env python3.7

"""Triple-quoted strings, while loop.

11 lines: Triple-quoted strings, while loop
from https://wiki.python.org/moin/SimplePrograms .

"""

REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
BOTTLES_OF_BEER = 9
while BOTTLES_OF_BEER > 1:
    print(REFRAIN % (BOTTLES_OF_BEER, BOTTLES_OF_BEER,
                     BOTTLES_OF_BEER - 1))
    BOTTLES_OF_BEER -= 1
