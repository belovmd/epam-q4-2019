"""List practice

1. Use a list comprehension to construct the list
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Use a slice on the above list to construct the list
    ['ab', 'ad', 'bc'].
3. Use a list comprehension to construct the list
    ['1a', '2a', '3a', '4a'].
4. Simultaneously remove the element '2a' from the above list
    and print it.
5. Copy the above list and add '2a' back into the list
    such that the original is still missing it.
"""

# 1
list1 = [ltr1 + ltr2 for ltr1 in 'ab' for ltr2 in 'bcd']
print(list1)

# 2
list2 = list1[::2]
print(list2)

# 3
list3 = [str(x) + 'a' for x in '12345']
print(list3)

# 4
print(list3.pop(1))
print(list3)

# 5
list4 = list3.copy()
list4.insert(1, '2a')
print(list3)
print(list4)
