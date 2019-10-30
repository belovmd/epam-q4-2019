def checkio(number: int) -> int:

    """Function should calculate the product of the digits excluding zeroes.

    For example: The number given is 123405. The result will be 1*2*3*4*5=120
    """
    number = str(number)
    prod = 1
    for num in number:
        if num == '0':
            continue
        else:
            prod *= int(num)
    return prod
