'''raise to the power args'''


def power(*args, power):
    new_list = [digit ** power for digit in args if type(digit) == int]
    return new_list


if __name__ == '__main__':
    print(*power(12, 44, 'daad', 67, 'sa', power=2))
