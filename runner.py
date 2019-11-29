import pytasks


def runner(a='', b='', c='', d=''):
    def combiner(x):
        if x == 'generate_numbers':
            print(pytasks.generate_numbers())
        elif x == 'count_characters':
            print(pytasks.count_characters())
        elif x == 'fizzbuzz':
            pytasks.fizzbuzz()
        elif x == 'is_palindrome':
            print(pytasks.is_palindrome())
        else:
            pass
    if a == '' and b == '' and c == '' and d == '':
        print(pytasks.generate_numbers())
        print(pytasks.count_characters())
        pytasks.fizzbuzz()
        print(pytasks.is_palindrome())
    else:
        combiner(a)
        combiner(b)
        combiner(c)
        combiner(d)
