"""List practice"""

# 1
list1 = [ltr1 + ltr2 for ltr1 in ['a', 'b'] for ltr2 in ['b', 'c', 'd']]
print(list1)

# 2
list2 = list1[::2]
print(list2)

# 3
list3 = [str(x) + 'a' for x in range(1, 5)]
print(list3)

# 4
print(list3.pop(1))
print(list3)

# 5
list4 = list3.copy()
list4.append('2a')
print(list3)
print(list4)
