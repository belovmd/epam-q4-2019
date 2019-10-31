"""Calculate the product of the digits excluding any zeroes."""


def checkio(number: int) -> int:
    a = str(number)
    result = 1
    for i in a:
        if i != "0":
            result *= int(i)
    return result


print(checkio(123405))
