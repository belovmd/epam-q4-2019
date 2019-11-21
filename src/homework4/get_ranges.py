"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
"""


def get_ranges(lst):
    result = []
    start = 0
    while start < len(lst):
        end = start
        while end < len(lst) - 1 and lst[end] == lst[end + 1] - 1:
            end += 1
        if start == end:
            result.append(str(lst[start]))
        else:
            result.append("{}-{}".format(lst[start], lst[end]))
        start = end + 1
    return ','.join(result)


assert get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == "0-4,7-8,10"
assert get_ranges([4, 7, 10]) == "4,7,10"
assert get_ranges([2, 3, 8, 9]) == "2-3,8-9"
