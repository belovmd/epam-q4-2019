"""Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""
from functools import reduce


# first solution
def get_ranges(int_list):
    return ",".join(reduce(gluing, int_list, []))


def gluing(res_lst, num):
    if res_lst:
        last = res_lst[-1].rpartition("-")[-1]
        if (int(last) + 1 == num):
            if res_lst[-1].isdigit():
                res_lst[-1] += "-" + str(num)
            else:
                res_lst[-1] = res_lst[-1].replace(last, str(num))
        else:
            res_lst.append(str(num))
    else:
        res_lst.append(str(num))
    return res_lst


# second solution
def get_ranges2(int_list):
    res = []
    length = len(int_list)
    l = r = 0
    while l < length:
        while r < length - 1 and int_list[r] + 1 == int_list[r + 1]:
            r += 1
        if l == r:
            res.append(str(int_list[l]))
        else:
            res.append(str(int_list[l]) + "-" + str(int_list[r]))
        l = r = r + 1
    return ",".join(res)
