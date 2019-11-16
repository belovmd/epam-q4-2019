"""
runner module can be imported or started from command line as script.
generate_numbers()
count_characters()
fizzbuzz() – returns list with values
is_palindrome() - returns True or False.
runner() function can be called as:
runner() – all functions will be called with default values
and result printed to screen
runner(‘generate_numbers’) – print result  only for generate_numbers()
runner(‘generate_numbers’, ‘happy_numbers’) – print results
for generate_numbers() and  happy_numbers().
Any combination of functions can be specified.
"""

import pytasks
import sys


def runner(*args):
    if not args:
        for attr in dir(pytasks):
            if not attr.startswith("__") and callable(getattr(pytasks, attr)):
                print(getattr(pytasks, attr)())
    else:
        for attr in args:
            if hasattr(pytasks, attr) and callable(getattr(pytasks, attr)):
                print(getattr(pytasks, attr)())
            else:
                print("Module pytasks has no function {}".format(attr))


if __name__ == "__main__":
    runner(*sys.argv[1:])
