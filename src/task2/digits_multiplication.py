"""Calculate the product of the digits excluding any zeroes."""


def checkio(number: int) -> int:
    a = str(number)
    result = 1
    for i in a:
        if i != "0":
            result *= int(i)
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
