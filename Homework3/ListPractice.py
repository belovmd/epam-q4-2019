""" List practice """

# 1)Use a list comprehension to construct the list
# ['ab', 'ac', 'ad','bb', 'bc', 'bd'].
lst1 = [symbol1 + symbol2 for symbol1 in "ab" for symbol2 in "bcd"]
print(lst1)

# 2)Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
lst2 = lst1[::2]
print(lst2)

# 3)Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
lst3 = [str(symbol1) + "a" for symbol1 in range(1, 5)]
print(lst3)

# 4)Simultaneously remove the element '2a' from the above list and print it.
print(lst3.pop(1))

# 5)Copy the above list and add '2a' back into the list such that the
#  original is still missing it.
lst4 = lst3.copy()
lst4.append("2a")
print("New list ", lst4)
print("Original ", lst3)
