"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    if len(lst) == 1:
        return str(lst[0])

    short_form = ''
    for pos in range(len(lst) - 1):
        prev = (lst[pos - 1] if pos != 0 else None)
        curr = lst[pos]
        nxt = lst[pos + 1]
        if curr != nxt - 1:
            curr = '(' + str(curr) + ')' if curr < 0 else str(curr)
            short_form += curr + ','
        elif prev is None or curr != prev + 1:
            short_form += str(curr) + '-'
    return short_form + str(lst[-1])
