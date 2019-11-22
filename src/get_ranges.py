"""Реализовать функцию get_ranges, которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список сворачивает"""


def get_ranges(lst):
    out_str = ''
    lenght = len(lst)
    for el in range(lenght):
        next_el = el + 1
        if next_el < lenght:
            value_next_el = lst[next_el] - 1
            if lst[el] == value_next_el:
                if out_str == '' or out_str[-1] == ',':
                    out_str += str(lst[el]) + '-'

            else:
                out_str += str(lst[el]) + ','
        else:
            out_str += str(lst[el])
    return out_str


if __name__ == '__main__':
    print(get_ranges([1, 2, 3, 6, 7, 8, 10, 11]))
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4, 7, 10]))
    print(get_ranges([2, 3, 8, 9]))
