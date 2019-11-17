def get_ranges(lst):
    """Function "get_ranges".

    This function takes list of unique sorted ascending integer numbers
    and returns this list rolled up.
    For example:
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    """
    pos = 0
    roll = str(lst[0])
    while pos <= len(lst) - 1:
        if pos == len(lst) - 1:
            if lst[pos] == lst[pos - 1] + 1:
                roll += '-' + str(lst[pos])
                break
            else:
                break
        elif lst[pos] + 1 == lst[pos + 1]:
            pos += 1
        elif lst[pos] - 1 == lst[pos - 1]:
            roll += '-' + str(lst[pos]) + ', ' + str(lst[pos + 1])
            pos += 1
        else:
            roll += ', ' + str(lst[pos + 1])
            pos += 1
    return roll
