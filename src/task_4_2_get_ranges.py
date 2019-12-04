"""Task_4_2."""

from itertools import groupby


class OneFromLast():
    """."""

    def __init__(self, first):
        """."""
        self.prev = first
        self.gr_id = first

    def __call__(self, value):
        """."""
        changed = +(value - self.prev) != 1
        self.prev = value
        if changed:
            self.gr_id = value
        return self.gr_id


def get_ranges(arr):
    """Decription.

    Реализовать функцию get_ranges которая получает на вход непустой
    список неповторяющихся целых чисел, отсортированных по возрастанию,
    которая этот список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
    """
    ranges = ''
    for gr_id, values in groupby(arr, OneFromLast(arr[0])):
        group_list = list(values)
        if len(group_list) == 1:
            ranges += wrap_num(group_list[0]) + ','
        else:
            ranges += wrap_num(group_list[0]) + '-' + \
                wrap_num(group_list[-1]) + ','
    return ranges[:-1]


def wrap_num(num):
    """Num to str, if num < 0 return (num)."""
    return str(num) if num >= 0 else '(' + str(num) + ')'


if __name__ == "__main__":
    print(wrap_num(1) == '1')
    print(wrap_num(-1) == '(-1)')
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == "0-4,7-8,10")
    print(get_ranges([4, 7, 10]) == "4,7,10")
    print(get_ranges([2, 3, 8, 9]) == "2-3,8-9")
    print(get_ranges([0, 1, 2, -3, 4, 7, 8, 10]) == "0-2,(-3),4,7-8,10")
