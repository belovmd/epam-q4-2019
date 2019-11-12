"""" List Practice """""

# ['ab','ac','ad','bb',' bc', 'db']
list_1 = [fir_el + sec_el for fir_el in 'ab' for sec_el in 'bcd']
print(list_1)

# ['ab', 'ad', 'bc']
list_2 = list_1[::2]
print(list_2)

# ['1a', '2a', '3a', '4a']
list_3_0 = [str(digit) + 'a' for digit in range(1, 5)]
list_3_1 = [sym + 'a' for sym in '1234']
list_3_2 = [str(num) + sym for num, sym in enumerate('a' * 4, 1)]
print('List_3_0:{0}'.format(list_3_0))
print('List_3_1:{0}'.format(list_3_1))
print('List_3_2:{0}'.format(list_3_2))

# Remove the element '2a' and print it
print(list_3_0.pop(1))
print(list_3_0)

# Copy the above list and add '2a' back into the list
list_4 = list_3_0.copy()
list_4.insert(1, '2a')
print(list_4)
