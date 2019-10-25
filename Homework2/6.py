"""
    sums even-indexes elements and multiply at the last
"""


def checkio(array):

    if len(array) == 0:
        return 0

    sum = 0
    element = 0
    for element in array[::2]:
        sum += element

    return sum * array[len(array) - 1]



print('Example:')
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0
