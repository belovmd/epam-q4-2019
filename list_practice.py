# 1. Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
lst1 = [x + y for x in 'ab' for y in 'bcd']

# 2. Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
lst1 = lst1[::2]

# 3. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
lst2 = [x + 'a' for x in '1234']

# 4. Simultaneously remove the element '2a' from the above list and print it.
lst2.pop(1)

# 5. Copy the above list and add '2a' back into the list
# such that the original is still missing it.
lst3 = lst2.copy()
lst3.insert(1, '2a')
