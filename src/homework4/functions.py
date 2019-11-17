"""Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""
from functools import reduce


# first solution, works only with positive numbers
def get_ranges(int_list):
    return ",".join(reduce(gluing, int_list, []))


def gluing(res_lst, num):
    if res_lst:
        last = res_lst[-1].split("-")[-1]
        if (int(last) + 1 == num):
            if res_lst[-1].isdigit():
                res_lst[-1] += "-{}".format(num)
            else:
                res_lst[-1] = res_lst[-1].replace(last, str(num))
        else:
            res_lst.append(str(num))
    else:
        res_lst.append(str(num))
    return res_lst


# second solution, works with all numbers
def get_ranges2(int_list):
    res = []
    length = len(int_list)
    start = 0
    while start < length:
        end = find_end(int_list, length, start)
        if start == end:
            res.append("{}".format(int_list[start]))
        else:
            res.append("{}-{}".format(int_list[start], braces(int_list[end])))
        start = end + 1
    return ",".join(res)


def braces(number):
    if number >= 0:
        return number
    else:
        return "({})".format(number)


def find_end(intlist, length, ptr):
    while ptr < length - 1 and intlist[ptr] + 1 == intlist[ptr + 1]:
        ptr += 1
    return ptr
