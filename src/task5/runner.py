"""Runs an prints functions from pytasks module

# Without arguments:  all functions
# With arguments: supplied functions"""


import pytasks
import types


def runner(*args):
    if len(args) == 0:
        for i in ([getattr(pytasks, a) for a in dir(pytasks)
                   if isinstance(getattr(pytasks, a), types.FunctionType)]):
            print(i())
    else:
        for arg in args:
            try:
                print(getattr(pytasks, arg)())
            except AttributeError as e:
                print(e)


# Examples
runner()
runner('generate_1numbers', 'fizzbuzz')
runner('dd')
runner('generate_1numbers', 'fizzbuzz')
