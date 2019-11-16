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

from pytasks import count_characters
from pytasks import generate_numbers
from pytasks import is_palindrome
from pytasks import fizzbuzz


def runner(*args):
    if not args:
        for func in generate_numbers, count_characters, fizzbuzz, is_palindrome:
            print(func())
    elif args == ('generate_numbers',):
        print(generate_numbers())
    elif args == ('generate_numbers', 'count_characters'):
        for func in generate_numbers, count_characters:
            print(func())
