"""Task 3 from Homework3 (dictionaries)"""


def generate_numbers(n=20):
    """Returns a dict, where the keys are numbers between 1 and n
    (both are included) and values are square of keys
    """

    return dict({key: key**2 for key in range(n + 1)[1:]})


def count_me_string(_str_):
    """Returns the numbers of each character in a count_me_string argument"""
    dct = {}

    for symbol in _str_:
        if symbol in dct:
            dct[symbol] += 1
        else:
            dct[symbol] = 1
    return dct


n = int(input("Enter n: "))
print(generate_numbers(n))

_str_ = input("string: ")
print(count_me_string(_str_))
