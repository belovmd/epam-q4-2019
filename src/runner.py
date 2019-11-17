""" Function runner can  de called as:
runner() – print results of all function
runner(‘generate_numbers’) – print result  only for generate_numbers()
runner(‘generate_numbers’, ‘happy_numbers’) – print results for gen_numbers()
and happy_numbers(). Any combination of functions can be specified."""

import pytasks
from random import choice


def runner(*funcs):
    module_funcs = dir(pytasks)
    module_funcs = [func for func in module_funcs if not func.startswith('__')]
    if not funcs:
        for func in module_funcs:
            print(getattr(pytasks, func)())
    elif 'happy_numbers' in funcs:
        for func in funcs:
            attr = hasattr(pytasks, func)
            if attr:
                print(getattr(pytasks, func)())
            elif not attr and func == 'happy_numbers':
                func = choice(module_funcs)
                print(getattr(pytasks, func)())
            else:
                print('My function : {0}'.format(','.join(module_funcs)))
    elif funcs:
        for func in funcs:
            print(getattr(pytasks, func)())


if __name__ == '__main__':
    runner('gen_numbers', 'happy_numbers', 'as')
    runner()
    runner('gen_numbers')
