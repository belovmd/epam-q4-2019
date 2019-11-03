list1 = [symbol1 + symbol2 for symbol1 in "ab" for symbol2 in "bcd"]
print(list1)

list2 = list1[::2]
print(list2)

list3 = [symbol1 + "a" for symbol1 in "1234"]
print(list3)

print(list3.pop(1))

list4 = list3.copy()
list4.insert(1, "2a")
print(list4)
