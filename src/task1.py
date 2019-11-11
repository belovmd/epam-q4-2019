"""task 1

Создайте декоратор, который хранит в себе результаты вызовов функций
и время получения результата за время запуска программы. """

import time

# global dictionary to sotre time and result of decorated functions runs.
decorator_run_statistic = dict()


# decorator
def run_and_save_decorator(funct):
    global decorator_run_statistic

    def wrapper(*args, **kwargs):
        rez = funct(*args, **kwargs)
        time_run = time.time()
        decorator_run_statistic[time_run] = rez
        return rez
    return wrapper


# first function to call
@run_and_save_decorator
def sum(a, b):
    return a + b


# second function to call
@run_and_save_decorator
def diff(a, b):
    return a - b


# test runs
print(sum(3, 8))
print(diff(31, 18))
print(sum(13, 8))
print("run stats: ", decorator_run_statistic)
