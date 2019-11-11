"""task 2

Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
 """


def get_ranges(lst):
    def append_range(list_to_add, item1, item2):
        if item1 == item2:
            list_to_add.append([item1])
        else:
            list_to_add.append([item1, item2])

    rez = list()
    start = lst[0]
    curr = lst[0]

    for x in lst:
        if x - curr <= 1:
            curr = x
        else:
            append_range(rez, start, curr)
            start = x
            curr = x
    append_range(rez, start, curr)
    return rez


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
