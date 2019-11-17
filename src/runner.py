# Модуль, использующий функции из pytasks.py
def runner(*functions):
    """Функция импорта из pytasks.py"""
    if not functions:
        from pytasks import generate_numbers, count_characters, \
                            fizzbuzz, is_palindrome
        print(generate_numbers())
        print(count_characters())
        print(fizzbuzz())
        print(is_palindrome())
    else:
        import pytasks
        for function_name in functions:
            if hasattr(pytasks, function_name):
                print(getattr(pytasks, function_name)())


runner()
runner('generate_numbers')
runner('generate_numbers', 'is_palindrome', 'count_characters', )