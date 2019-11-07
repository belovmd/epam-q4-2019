"""" List Practice  """""

# ['ab','ac','ad','bb',' bc', 'db']
list_1 = [fir + sec_el for fir_el in 'ab' for sec_el in 'bcd']
print(list_1)

# ['ab', 'ad', 'bc']
list_2 = list_1[::2]
print(list_2)

# ['1a', '2a', '3a', '4a']
list_3 = [str(digit) + 'a' for digit in range(1, 5)]
print(list_3)

# Remove the element '2a' and print it
print(list_3.pop(1))
print(list_3)

# Copy the above list and add '2a' back into the list
list_4 = list_3.copy()
list_4.insert(1, '2a')
print(list_4)
