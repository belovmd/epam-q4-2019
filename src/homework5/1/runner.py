import inspect
import pytasks


def runner(*args):
    if not args:
        func_tuples = inspect.getmembers(pytasks, inspect.isfunction)
        args = [f[-1] for f in func_tuples]  # get function object
    else:
        args = [getattr(pytasks, func_str) for func_str in args]
    for func in args:
        print(func())
