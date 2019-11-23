from pytasks import generate_numbers
from pytasks import count_characters
from pytasks import is_palindrome
from pytasks import fizz_buzz
import pytasks


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
