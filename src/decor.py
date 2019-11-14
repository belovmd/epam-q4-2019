""" Создать декоратор, который хранит в себе результы вызовов
функций и время получения программы за время запуска """

from collections import defaultdict
from time import time

data = defaultdict(list)


def storage(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        data[func.__name__].extend([res, start_time - time()])
        return res

    return wrapper


@storage
def sum_(*args):
    return sum(args)


@storage
def hi():
    return 'Hi'


if __name__ == '__main__':
    print((sum_(1, 2, 3)))
    print(storage(sum_)(1, 2, 3))
    print(hi())
    print(data)
