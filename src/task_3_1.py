"""List practice."""

# 1. Use a list comprehension to construct
# the list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
PRACTICE_LIST = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']

# 2. Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
SLICE_LIST = PRACTICE_LIST[0:5:2]

# 3. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
PRACTICE_LIST_2 = ['1a', '2a', '3a', '4a']

# 4. Simultaneously remove the element '2a' from the above list and print it.
print(PRACTICE_LIST_2.pop(1))

# 5. Copy the above list and add '2a' back into the list
# such that the original is still missing it.
COPY_PRACTICE_LIST_2 = PRACTICE_LIST_2.copy()

COPY_PRACTICE_LIST_2.append('2a')  # or COPY_PRACTICE_LIST_2.insert(1, '2a')
