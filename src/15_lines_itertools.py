#!/usr/bin/env python3.7

"""Itertools.

15 lines: itertools from https://wiki.python.org/moin/SimplePrograms .

"""

from itertools import groupby
LINES = '''
This is the
first paragraph.

This is the second.
'''.splitlines()
# Use itertools.groupby and bool to return groups of
# consecutive lines that either have content or don't.
for has_chars, frags in groupby(LINES, bool):
    if has_chars:
        print(' '.join(frags))
# PRINTS:
# This is the first paragraph.
# This is the second.
