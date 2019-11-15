"""
Создайте декоратор, который хранит в себе результаты вызовов
функций и время получения результата за время запуска программы.
"""

import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        time.sleep(3)
        res = func(*args, **kwargs)
        return res, time.time() - start_time
    return wrapper


@my_decorator
def reverse_string(string):
    return string[::-1]


print(reverse_string("Создайте декоратор"))
