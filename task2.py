def index_power(array: list, n: int) -> int:
    """Find N-th power of the element with index N."""
    if n > len(array) - 1:
        return -1
    else:
        return array[n] ** n
