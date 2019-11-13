"""
Создайте декоратор, который хранит в себе результаты вызовов функций
и время получения результата за время запуска программы.
"""

import time


def log_results(lst):
    def decorator(func):
        def wrapper(*args, **kwargs):
            before = time.time()
            result = func(*args, **kwargs)
            exec_time = time.time() - before
            lst.append([result, exec_time])
            return result
        return wrapper
    return decorator
