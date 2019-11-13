from time import time

registry = {}


def wrapper(func):
    def timer(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        stop = time()
        registry[func.__name__] = (
            "result: {result}; function execution time: {timer}".format
            (result=res, timer=stop - start))
        return res

    return timer


@wrapper
def spam(*args):
    return {arg: arg ** 2 for arg in args}  # spam = wrapper(spam)


@wrapper
def get_ranges(lst):
    """Function "get_ranges".

    This function takes list of unique sorted ascending integer numbers
    and returns this list rolled up.
    For example:
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    """
    pos = 0
    rolled_list = str(lst[0])
    while pos <= len(lst) - 1:
        if pos == len(lst) - 1:
            rolled_list += '-' + str(lst[pos])
            break
        elif lst[pos] + 1 == lst[pos + 1]:
            pos += 1
        elif lst[pos] - 1 == lst[pos - 1]:
            rolled_list += '-' + str(lst[pos]) + ', ' + str(lst[pos + 1])
            pos += 1
        else:
            rolled_list += ', ' + str(lst[pos + 1])
            pos += 1
    return rolled_list


@wrapper
def count_characters(s):
    """Function count and return the numbers of each character in a string."""
    dct = {}
    for symb in s:
        dct[symb] = dct.get(symb, 0) + 1
    return dct


if __name__ == "__main__":
    spam(1, 2, 3)
    get_ranges([1, 2, 3, 5, 10, 11, 14, 15, 16])
    count_characters('ds[pfpkefw[efkas[eofkjsdkvna')
    for func in registry:
        print('Function ' + func + ' ===>', registry[func])
