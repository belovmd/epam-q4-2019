# 1.1 construct list with list comprehension
list_1 = [letter1 + letter2 for letter1 in 'ab' for letter2 in 'bcd']
assert list_1 == ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
print(list_1)

# 1.2 slice list
list_1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
list_2 = list_1[:5:2]
assert list_2 == ['ab', 'ad', 'bc']
print(list_2)

# 1.3 construct list with list comprehension
list_3 = [el + 'a' for el in '1234']
assert list_3 == ['1a', '2a', '3a', '4a']
print(list_3)

# 1.4 remove element from the list
list_4 = ['1a', '2a', '3a', '4a']
list_4.remove('2a')
assert list_4 == ['1a', '3a', '4a']
print(list_4)

list_4 = ['1a', '2a', '3a', '4a']
removed_el = list_4.pop(1)
assert list_4 == ['1a', '3a', '4a']
print(removed_el)
print(list_4)

# 1.5 Copy and modify list
list_4 = ['1a', '3a', '4a']
list_5 = list_4.copy()
list_5.insert(1, '2a')
assert list_4 == ['1a', '3a', '4a']
assert list_5 == ['1a', '2a', '3a', '4a']
print(list_5)
