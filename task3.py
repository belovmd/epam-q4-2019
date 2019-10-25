def checkio(number: int) -> int:
    """Calculate the product of the digits excluding any zeroes."""
    number = str(number)
    prod = 1
    for num in number:
        if num == '0':
            continue
        else:
            prod *= int(num)
    return prod
