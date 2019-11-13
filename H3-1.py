"""
List practice
"""
# Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
list1 = [e1 + e2 for e1 in 'ab' for e2 in 'bcd']
print(list1)

# Use a slice on the above list to construct
# the list ['ab', 'ad', 'bc'].
list2 = list1[::2]
print(list2)

# Use a list comprehension to construct
# the list ['1a', '2a', '3a', '4a'].
list3 = [e1 + e2 for e1 in '1234' for e2 in 'a']
print(list3)

# Simultaneously remove the element '2a'
# from the above list and print it.
print(list3.pop(1))

# Copy the above list and add '2a' back into the
# list such that the original is still missing it.
list4 = list3.copy()
list4.insert(1, '2a')
print(list4)
