""" Write two modules pytasks.py and runner.py. Module pytasks contains
definition for functions from previous tasks.  Separate module runner
contains runner() function. runner module can be imported or started
from command line as script.
generate_numbers()
count_characters()
fizzbuzz() – returns list with values
is_palindrome() - returns True or False.
runner() function can be called as:
runner() – all functions will be called with default values and result
printed to screen
runner(‘generate_numbers’) – print result  only for generate_numbers()
runner(‘generate_numbers’, ‘count_characters’) – print results for
generate_numbers() and  count_characters(). Any combination of functions
can be specified. """

import pytasks


def runner(*args):
    if args:
        for func in args:
            if hasattr(pytasks, func) and callable(getattr(pytasks, func)):
                print(getattr(pytasks, func)())
    else:
        for atr in dir(pytasks):
            if callable(getattr(pytasks, atr)) and not atr.startswith('__'):
                print(getattr(pytasks, atr)())
