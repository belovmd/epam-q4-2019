#!/usr/bin/env python3.7

"""Indent your Python code to put into an email.

9 lines: Opening files from https://wiki.python.org/moin/SimplePrograms .

"""

import glob
# glob supports Unix style pathname extensions
PYTHON_FILES = glob.glob('*.py')
for file_name in sorted(PYTHON_FILES):
    print('    ------' + file_name)

    with open(file_name) as f:
        for line in f:
            print('    ' + line.rstrip())

    print()
