""" Dictionary practice """

from collections import Counter


# key is number, value is the square of  this number
def gen_numbers(numbers=20):
    return {digit: digit ** 2 for digit in range(1, numbers + 1)}


# key is character, value is quantity of this character
def count_characters(str_):
    return {sym: str_.count(sym) for sym in set(str_)}


def count_characters2(str_):
    return dict(Counter(str_))


def count_characters3(str_):
    dict_ = {}
    for sym in str_:
        dict_[sym] = dict_.get(sym, 0) + 1
    return dict_


if __name__ == '__main__':
    print(gen_numbers())
    print(count_characters('abcdefgabc'))
    print(count_characters2('abcdefgabc'))
    print(count_characters3('abcdefgabc'))
