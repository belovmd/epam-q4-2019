"""Task from checkio - 'Sort Array by Element Frequency'
Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency,
they should end up in the same order as the first appearance in the iterable.
"""


def frequency_sort(items):
    dct = dict.fromkeys(items, 0)
    lst = []

    for elem in items:
        dct[elem] += 1

    for key, value in sorted(dct.items(), key=lambda item: item[1], reverse=True):
        for i in range(value):
            lst.append(key)

    return lst


print("Example:")
print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
