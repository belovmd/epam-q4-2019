"""
Создайте декоратор, который хранит в себе
результаты вызовов функций и время получения
результата за время запуска программы
"""
import time


def timer(f):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = f(*args, **kwargs)
        t1 = time.time()
        return res
    return wrapper


@timer
def func(x, y):
    return x + y


print(func(2, 4))
