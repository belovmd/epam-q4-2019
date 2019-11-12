"""
Создайте декоратор, который хранит в себе результаты вызовов функций и
время получения результата за время запуска программы.
"""

from time import gmtime
from time import sleep
from time import strftime


def func_calls_history(func):
    calls_history = []  # don't use nonlocal in wrapper because list is mutable

    def wrapper(*args, **kwargs):
        func_call_result = func(*args, **kwargs)
        calls_history.append({'func': func.__name__,
                              'end_time': strftime("%Y-%m-%d %T", gmtime()),
                              'result': func_call_result
                              })
        sleep(1)
        return func_call_result
    return wrapper
