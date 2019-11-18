""" Function runner can  de called as:
runner() – print results of all function
runner(‘generate_numbers’) – print result  only for generate_numbers()
runner(‘generate_numbers’, ‘happy_numbers’) – print results for gen_numbers()
and happy_numbers(). Any combination of functions can be specified."""

import pytasks
from random import choice


def runner(*funcs):
    module_funcs = dir(pytasks)
    module_funcs = [func for func in module_funcs
                    if not func.startswith('__') and
                    callable(getattr(pytasks, func))]
    if not funcs:
        for func in module_funcs:
            print(getattr(pytasks, func)())

    else:
        for func in funcs:
            try:
                if func == 'happy_numbers':
                    func = choice(module_funcs)
                    print(getattr(pytasks, func)())
                else:
                    print(getattr(pytasks, func)())
            except AttributeError:
                print('Function {0} not found'.format(func))


if __name__ == '__main__':
    runner('gen_numbers', 'happy_numbers', 'as')
    runner()
    runner('gen_numbers')
