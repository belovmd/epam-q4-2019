def get_ranges(lst):
    diff, first = lst[0], lst[0]
    ans = str(lst[0])
    for i in range(len(lst)):
        if lst[i] == i + diff:
            if i == len(lst) - 1:
                ans += "-" + str(lst[i])
        else:
            if first != lst[i - 1]:
                ans += "-" + str(lst[i - 1]) + "," + str(lst[i])
            else:
                ans += "," + str(lst[i])
            diff = lst[i] - i
            first = lst[i]
    return ans


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
