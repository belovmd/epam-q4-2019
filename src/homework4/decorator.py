"""
Создайте декоратор, который хранит в себе результаты вызовов функций
и время получения результата за время запуска программы.
"""

import time


def log_results(func):
    if not hasattr(log_results, "logs"):
        log_results.logs = []

    def wrapper(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        exec_time = time.time() - before
        log_results.logs.append({"result": result, "exec_time": exec_time})
        return result

    return wrapper
