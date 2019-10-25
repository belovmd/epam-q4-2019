def checkio(array):
    """sums even-indexes elements and multiply at the last."""
    sum = 0
    if array == []:
        return 0
    else:
        for elem in array[::2]:
            sum += elem

        return sum * array[-1]
