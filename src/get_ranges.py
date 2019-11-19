"""Реализовать функцию get_ranges, которая получает на вхох непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список сворачивает"""


def get_ranges(lst):
    out_str = ''
    lenght = len(lst)
    for el in range(lenght):
        if el + 1 < lenght:
            if lst[el] == lst[el + 1] - 1:
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
