def generate_numbers(n=20):
    """Function returns dictionary.

    The keys are numbers between 1 and n (both included) and the values
    are square of keys. n – function argument. Default is 20.
    """
    return {num: num**2 for num in range(1, n + 1)}


def count_characters(s):
    """Function count and return the numbers of each character in a string."""
    dct = {}
    for symb in s:
        if symb in dct:
            dct[symb] += 1
        else:
            dct[symb] = 1
    return dct
