"""Decorator that keeps result of function and its execution time"""

import time


def timer(f):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = f(*args, **kwargs)
        t1 = time.time()
        function_execution_time = t1 - t0
        print(function_execution_time)
        return res
    return wrapper


@timer
def count_characters(count_me_string):
    try:
        count_me_string = str(count_me_string)
    except Exception:
        raise Exception
    if len(count_me_string) == 0:
        raise ValueError('Empty string input is not allowed')

    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890,.;'
    count_me_string = count_me_string.lower()
    return {letter: count_me_string.count(letter)
            for letter in alphabet
            if count_me_string.count(letter) > 0}


if __name__ == "__main__":
    print(count_characters('Neonatal Intensive Care Unit'))
