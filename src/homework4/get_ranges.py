"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
"""


def get_ranges(lst):
    result = ""
    start, prev = lst[0], lst[0]
    for num in lst[1:]:
        if num - prev != 1:
            result += str(start) + ('-' + str(prev)) * (prev != start) + ','
            start = num
        prev = num

    return result + str(start) + ('-' + str(prev)) * (prev != start)


assert get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == "0-4,7-8,10"
assert get_ranges([4, 7, 10]) == "4,7,10"
assert get_ranges([2, 3, 8, 9]) == "2-3,8-9"
