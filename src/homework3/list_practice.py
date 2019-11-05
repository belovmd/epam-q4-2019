""" List practice """

# Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
lst = [ab + bcd for ab in "ab" for bcd in "bcd"]

# Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
slc = lst[::2]

# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
lst2 = [str(i) + 'a' for i in range(1, 5)]

# Simultaneously remove the element '2a' from the above list and print it.
print(lst2.pop(1))

# Copy the above list and add '2a' back into the list such
# that the original is still missing it.
lst2_copy = lst2[:]
lst2_copy.insert(1, "2a")
