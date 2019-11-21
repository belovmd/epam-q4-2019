import pytasks


def runner(*functions):
    """runner

    Called function(s) from pytasks module with default values and printed
    results to screen.
    runner() calls all functions from pytasks
    """

    if not functions:
        functions = [fun for fun in dir(pytasks) if not fun.startswith('__')]
    for func in functions:
        if hasattr(pytasks, func):
            if callable(getattr(pytasks, func)):
                print('{}: {}'.format(func, getattr(pytasks, func)()))
        else:
            print('There is no {} function in pytasks module'.format(func))
