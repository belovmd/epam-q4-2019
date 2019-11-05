"""Play around  with lists"""

# Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
list1 = [ltr + ltr2 for ltr in "ab" for ltr2 in "bcd"]
print(list1)

# Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
list2 = list1[::2]
print(list2)

# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
list3 = [str(dgt) + "a" for dgt in range(1, 5)]
print(list3)

# Simultaneously remove the element '2a' from the above list and print it.
print("deleted element:", list3.pop(1))

# Copy the above list and add '2a' back into the list such that
# the original is still missing it.
list4 = list3.copy()
list4.insert(1, "2a")
print("list4:", list4)
print("list3", list3)
