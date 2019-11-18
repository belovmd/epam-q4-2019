"""Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список 'сворачивает'"""


def get_ranges(lst):
    first = lst[0]
    last = first
    glued = ""
    for elem in lst[1:]:
        if elem == last + 1:
            last += 1
        else:
            if first != last:
                glued += str(first) + "-" + str(last) + ","
            else:
                glued += str(first) + ","
            first = elem
            last = first

    if first != last:
        glued += str(first) + "-" + str(last)
    else:
        glued += str(first)

    return glued


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
