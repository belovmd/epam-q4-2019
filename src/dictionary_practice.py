""" Dictionary practice """


# key is number, value is the square of  this number
def gen_numbers(numbers=20):
    return {digit: digit ** 2 for digit in range(1, numbers + 1)}


# key is character, value is quantity of this character
def count_characters(str_):
    return {sym: str_.count(sym) for sym in set(str_)}


if __name__ == '__main__':
    print(gen_numbers())
    print(count_characters('abcdefgabc'))
