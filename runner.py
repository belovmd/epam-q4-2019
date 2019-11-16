import pytasks


def runner(*functions):
    """runner

    Called function(s) from pytasks module with default values and printed
    results to screen.
    runner() calls all functions from pytasks"""

    if not functions:
        functions = dir(pytasks)
    for func in functions:
        if not func.startswith('__'):
            if hasattr(pytasks, func):
                print('{}: {}'.format(func, getattr(pytasks, func)()))
            else:
                print('There is no {} function in pytasks module'.format(func))
