import HWs2_5


def runner(*functions):
    """runner

    Called function(s) from pytasks module with default values and printed
    results to screen.
    runner() calls all functions from pytasks
    """

    result = []
    if not functions:
        functions = [fun for fun in dir(HWs2_5) if not fun.startswith('__')]
    for func in functions:
        if hasattr(HWs2_5, func):
            if callable(getattr(HWs2_5, func)):
                print('{}: {}'.format(func, getattr(HWs2_5, func)()))
                result.append(getattr(HWs2_5, func)())
    return result
