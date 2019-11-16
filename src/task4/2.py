"""Function, that receives not empty list of non-repeating integers,
 sorted descending and "shortens" the list"""


def get_ranges(my_list):
    a = b = None
    res = ""
    for i in my_list:
        if a is None and b is None:
            a = b = i
        elif i == b or i == b + 1:
            b = i
        else:
            if a == b:
                res += '{},'.format(a)
            else:
                res += '{}-{},'.format(a, b)
            a = b = i
    if a is not None and b is not None:
        if a == b:
            res += '{}'.format(a)
        else:
            res += '{}-{}'.format(a, b)
    return res

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
assert get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == "0-4,7-8,10"
assert get_ranges([4, 7, 10]) == "4,7,10"
assert get_ranges([2, 3, 8, 9]) == "2-3,8-9"
