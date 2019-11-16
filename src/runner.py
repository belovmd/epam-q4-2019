import pytasks
from random import choice


def runner(*funcs):
    pytasks_funcs = dir(pytasks)
    pytasks_funcs = [func for func in pytasks_funcs if not func.startswith('__')]
    if not funcs:
        for func in pytasks_funcs:
            print(getattr(pytasks, func)())
    elif 'happy_numbers' in funcs:
        for func in funcs:
            attr = hasattr(pytasks, func)
            if attr:
                print(getattr(pytasks, func)())
            elif not attr and func == 'happy_numbers':
                func = choice(pytasks_funcs)
                print(getattr(pytasks, func)())
            else:
                print('Function not found, my function : {0}'. format(','.join(pytasks_funcs)))
    elif funcs:
        for func in funcs:
            print(getattr(pytasks, func)())


if __name__ == '__main__':
    runner('gen_numbers', 'happy_numbers', 'adsa')
    runner()
    runner('gen_numbers')
