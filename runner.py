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
from pytasks import fizz_buzz
from pytasks import is_palindrome
import pytasks
from pytasks import generate_numbers


def runner(*func):
    if not func:
        print(generate_numbers())
        print(count_characters())
        print(is_palindrome())
        print(fizz_buzz())
    else:
        for i in func:
            if hasattr(pytasks, i):
                method_to_call = getattr(pytasks, i)
                print(method_to_call())


runner()
runner('generate_numbers')
runner('count_characters')
runner('is_palindrome', 'count_characters', 'fizz_buzz')
