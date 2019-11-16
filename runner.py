import pytasks


def runner(*args):
    """Function prints result of args taken function."""
    if not args:
        pytasks.main()
    else:
        for func_name in args:
            if hasattr(pytasks, func_name):
                method_to_call = getattr(pytasks, func_name)
                method_to_call()
            else:
                print(func_name, 'Name doesn\'t exist')


# Uncomment to use the second solution
# x = [pytasks.generate_numbers,
#      pytasks.count_characters,
#      pytasks.is_palindrome,
#      pytasks.fiz_buzz]


# def runner(*args):
#     """Function prints result of args taken function."""
#     if not args:
#         for func in x:
#             func()
#     else:
#         for func_name in args:
#             for func in x:
#                 if func_name == func.__name__:
#                     func()
#                 else:
#                     print(func_name, 'Name doesnt exist')


runner()
print('-'*79)
runner('generate_numbers')
print('-'*79)
runner('fiz_buzz', 'count_character')
print('-'*79)
runner('is_palindrome', 'count_characters', 'generate_numbers')
