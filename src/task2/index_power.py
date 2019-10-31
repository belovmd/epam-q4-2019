"""Find the N-th power of the element in the array with the index N.

If N is outside of the array, then return -1.
"""


def index_power(array: list, n: int) -> int:
    if n < len(array):
        return array[n] ** n
    else:
        return -1


print(index_power([1, 2, 3, 4], 2))
