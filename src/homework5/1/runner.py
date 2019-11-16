from inspect import isfunction
import pytasks


def runner(*args):
    if not args:
        args = [attr for attr in dir(pytasks) if not attr.startswith("__")]
    [print(getattr(pytasks, func)()) for func in args if
     isfunction(getattr(pytasks, func))]
