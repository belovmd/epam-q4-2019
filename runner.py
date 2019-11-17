"""Write two modules pytasks.py and runner.py.

Module pytasks contains definition for functions from previous tasks.
Separate module runner contains runner() function.
runner module can be imported or started from command line as script.
runner() function can be called as:
runner() – all functions will be called with default values and result printed
to screen
runner(‘generate_numbers’) – print result  only for generate_numbers()
runner(‘generate_numbers’, ‘happy_numbers’) – print results for
generate_numbers() and  happy_numbers(). Any combination of functions can be
specified.
"""
import pytasks


def runner(*args):
    """Function prints result of args taken function."""
    if not args:
        pytasks.generate_numbers()
        pytasks.is_palindrome()
        pytasks.fiz_buzz()
        pytasks.count_characters()
    else:
        for func_name in args:
            if hasattr(pytasks, func_name):
                method_to_call = getattr(pytasks, func_name)
                method_to_call()
            else:
                print(func_name, 'Name doesn\'t exist')


runner()
print('-' * 79)
runner('generate_numbers')
print('-' * 79)
runner('fiz_buzz', 'count_character')
print('-' * 79)
runner('is_palindrome', 'count_characters', 'generate_numbers')
