"""Write two modules pytasks.py and runner.py. Module pytasks contains
definition for functions from previous tasks.  Separate module runner
contains runner() function. runner module can be imported or started from
command line as script.
generate_numbers()
count_characters()
fizzbuzz() – returns list with values
is_palindrome() - returns True or False.
runner() function can be called as:
runner() – all functions will be called with default values and result
printed to screen
runner(‘generate_numbers’) – print result  only for generate_numbers()
runner(‘generate_numbers’, ‘happy_numbers’) – print results for
generate_numbers() and  happy_numbers(). Any combination of functions can be
specified."""
import pytasks


def runner(*functions):
    """Функция импорта из pytasks.py"""
    if not functions:
        for func in dir(pytasks):
            if callable(getattr(pytasks, func)):
                print(getattr(pytasks, func)())

    else:
        for function_name in functions:
            if hasattr(pytasks, function_name) and (
                    callable(getattr(pytasks, function_name))):
                print(getattr(pytasks, function_name)())


runner()
runner('generate_numbers')
runner('generate_numbers', 'is_palindrome', 'count_characters', )
