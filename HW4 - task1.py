"""
Создайте декоратор, который хранит в себе результаты вызовов функций и
время получения результата за время запуска программы.
"""

from time import gmtime
from time import sleep
from time import strftime


def func_calls_history_v1(func):
    """decorator which save history for all functions

    There is decision for first version of task - decorator save all functions
    called during program running
    """
    if not hasattr(func_calls_history_v1, 'calls_history'):
        func_calls_history_v1.calls_history = []

    def wrapper(*args, **kwargs):
        func_call_result = func(*args, **kwargs)
        func_calls_history_v1.calls_history.append({
            'func': func.__name__,
            'end_time': strftime("%Y-%m-%d %T", gmtime()),
            'result': func_call_result
            })
        sleep(1)
        return func_call_result
    return wrapper


def func_calls_history_v2(func):
    """decorator which save history for one function

    There is decision for second version of task - decorator save just calls of
    one function. If another function called, calls_history will reset
    """
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
