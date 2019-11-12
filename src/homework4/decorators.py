"""Создайте декоратор, который хранит в себе результаты вызовов функций и
время получения результата за время запуска программы."""
import time

result = []


def store(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        for i in range(1000):  # to make time bigger
            res = f(*args, **kwargs)
        stop = time.time()
        result.append({"result": res % (10 ** 8), "time": (stop - start)})

    return wrapper


@store
def pow(a, b):
    return a ** b


for i, j in zip(range(10 ** 2), range(10 ** 3)):
    pow(i, j)
print(result)
