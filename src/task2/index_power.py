"""Find the N-th power of the element in the array with the index N.

If N is outside of the array, then return -1.  """


def index_power(array: list, n: int) -> int:
    if n < len(array):
        return array[n] ** n
    else:
        return -1


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
