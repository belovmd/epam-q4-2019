import pytasks


def runner(*args):
    if not args:
        funcs = [getattr(pytasks, elem) for elem in dir(pytasks)
                 if not elem.startswith("__")]
        for func in funcs:
            print(func())
    else:
        for elem in args:
            print(getattr(pytasks, elem)())
