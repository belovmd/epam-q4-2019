"""Task_4_1.

Создайте декоратор, который хранит в себе результаты вызовов функции
и время получения результата за время запуска программы.

Not correct task.
"""

from datetime import datetime


def func_logs(func):
    """Save func logs .

    Decorator which save logs for last sequence call of one function.
    """
    logs = []

    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        logs.append({'func_name': func.__name__,
                     'end_time': str(datetime.now()),
                     'func_result': func_result
                     })
        return func_result
    return wrapper


if __name__ == '__main__':

    @func_logs
    def print_args(*args):
        """Print arguments."""
        for arg in args:
            print(arg)

    @func_logs
    def print_args_2(*args):
        """Print arguments."""
        for arg in args:
            print(arg)

if __name__ == '__main__':
    print(print_args(1))
    print(print_args(2))
    print(print_args_2(3, 2))
    print(print_args(4))
