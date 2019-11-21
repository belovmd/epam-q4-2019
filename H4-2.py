"""
Реализовать функцию get_ranges
которая получает на вход непустой список
неповторяющихся целых чисел,
отсортированных по возрастанию,
которая этот список “сворачивает”
"""


def get_ranges(list):
    new_list = ""
    for i in range(len(list) - 1):
        if line[i] + 1 != list[i + 1]:
            new_list += str(list[i]) + ","
        elif list[i] - 1 != list[i - 1]:
            new_list += str(list[i]) + "-"
    new_list += str(list[-1])
    return new_list


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  # "0-4,7-8,10"
print(get_ranges([4, 7, 10]))  # "4,7,10"
print(get_ranges([2, 3, 8, 9]))  # "2-3,8-9"
