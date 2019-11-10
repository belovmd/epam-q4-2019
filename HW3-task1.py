"""List practice
1. Use a list comprehension to construct the list ['ab', 'ac', 'ad', 'bb',
'bc', 'bd'].
2. Use a slice on the above list to construct the list  ['ab', 'ad', 'bc'].
3. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
4. Simultaneously remove the element '2a' from the above list and print it.
5. Copy the above list and add '2a' back into the list such that the original
is still missing it. """


list1 = [lett1 + lett2 for lett1 in 'ab' for lett2 in 'bcd']
sliced_list = list1[::2]

list2 = [pos + 'a' for pos in '1234']

number_to_pop = list2.index('2a')
print(list2.pop(number_to_pop))

list2_copy = list2.copy()
list2_copy.insert(number_to_pop, '2a')
