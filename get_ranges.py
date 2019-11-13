def get_ranges(lst):
    """
    Function "get_ranges".

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
