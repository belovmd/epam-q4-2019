"""Создайте декоратор, который хранит в себе результаты вызовов функций и
время получения результата за время запуска программы."""

import time
log = []


def timer(f):
    def wrapper(*args, **kwargs):
        global log
        t0 = time.time()
        res = f(*args, **kwargs)
        t1 = time.time()
        log.append({"function_name": f.__name__,
                    "result": res,
                    "execution_time": t1 - t0,
                    })
        return res
    return wrapper


@timer
def func1(x, y):
    return x + y


@timer
def func2(x, y):
    return x - y


func1(3, 2)
func2(3, 2)
print(log)
