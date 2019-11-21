"""
Создайте декоратор, который хранит в себе результаты вызовов
функций и время получения результата за время запуска программы.
"""

import time


def my_decorator(func):
    result = []

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        result.append({"Result": res,
                       "Time": time.time() - start_time})
        return result
    return wrapper


@my_decorator
def reverse_string(string):
    return string[::-1]


print(reverse_string("Создайте декоратор"))
