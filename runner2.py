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

x = {}
for method in dir(pytasks):
    if not method.startswith('__') and callable(getattr(pytasks, method)):
        x[str(method)] = getattr(pytasks, method)


def runner2(*args):
    """Function prints result of args taken function."""
    if not args:
        for func in x.values():
            func()
    else:
        for func_name in args:
            if func_name in x.keys():
                x[func_name]()
            else:
                print(func_name, 'Name doesnt exist')


runner2()
print('-' * 79)
runner2('generate_numbers')
print('-' * 79)
runner2('fiz_buzz', 'count_character')
print('-' * 79)
runner2('is_palindrome', 'count_characters', 'generate_numbers')
