"""
Write two modules pytasks.py and runner.py. Module pytasks
contains definition for functions from previous tasks.
Separate module runner contains runner() function. runner
module can be imported or started from command line as script.
generate_numbers()
count_characters()
fizzbuzz() – returns list with values
is_palindrome() - returns True or False.
runner() function can be called as:
runner() – all functions will be called with default values
 and result printed to screen
runner(‘generate_numbers’) – print result  only for generate_numbers()
runner(‘generate_numbers’, ‘happy_numbers’) – print results
for generate_numbers() and  happy_numbers(). Any combination
of functions can be specified.
"""
import pytasks
import sys


def runner(*args):
    if not args:
        args = [attr for attr in dir(pytasks) if not attr.startswith("__")]
    for arg in args:
        if hasattr(pytasks, arg) and callable(getattr(pytasks, arg)):
            print(getattr(pytasks, arg)())


if __name__ == '__main__':
    runner(*sys.argv[1:])
