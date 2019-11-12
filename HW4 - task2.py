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

    new_lst = ''
    for pos in range(len(lst) - 1):
        if lst[pos] != lst[pos + 1] - 1:
            new_lst += str(lst[pos]) + ','
        elif pos == 0 or lst[pos] != lst[pos - 1] + 1:
            new_lst += str(lst[pos]) + '-'
    return new_lst + str(lst[-1])
