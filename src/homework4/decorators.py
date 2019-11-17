"""Создайте декоратор, который хранит в себе результаты вызовов функций и
время получения результата за время запуска программы."""
import time

result = []


def store(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        stop = time.time()
        result.append({"result": res, "time": (stop - start)})

    return wrapper


@store
def pow(a, b):
    return a ** b


[pow(11111 ** 1111, j) for j in range(10)]
[print(r) for r in result]


# another solution, sort of cache
def store2(f):
    result2 = {}

    def wrapper(*args, **kwargs):
        if args in result2:
            return result2[args].result
        else:
            start = time.time()
            res = f(*args, **kwargs)
            stop = time.time()
            result2[args] = {"result": res, "time": (stop - start)}
            return result2[args]

    return wrapper


@store2
def pow2(a, b):
    return a ** b


[print(pow2(11111 ** 1111, j)) for j in range(10)]
