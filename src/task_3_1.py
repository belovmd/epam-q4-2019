"""List practice."""

# 1. Use a list comprehension to construct
# the list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
LIST_1 = [letter_1 + letter_2 for letter_1 in 'ab' for letter_2 in 'bcd']

# 2. Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
SLICE_LIST_1 = LIST_1[::2]

# 3. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
list_2 = [idx + 'a' for idx in '1234']

# 4. Simultaneously remove the element '2a' from the above list and print it.
print(list_2.pop(1))

# 5. Copy the above list and add '2a' back into the list
# such that the original is still missing it.
copy_list_2 = list_2.copy()

copy_list_2.append('2a')  # or copy_list_2.insert(1, '2a')
