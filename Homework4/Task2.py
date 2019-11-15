"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    res = ""
    start_el = lst[0]
    for pos, element in enumerate(lst[1:]):
        if element - lst[pos] != 1:
            res += \
                str(start_el) + ("-" + str(lst[pos])) * \
                (start_el != lst[pos]) + ","
            start_el = element
    return res + str(start_el) + ("-" + str(element)) * (start_el != element)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
