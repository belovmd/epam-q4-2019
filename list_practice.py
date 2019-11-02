lst1 = [x + y for x in ('a', 'b') for y in ('b', 'c', 'd')]
lst1 = lst1[::2]
lst2 = [x + 'a' for x in ('1', '2', '3', '4')]
lst2.pop(1)
lst3 = lst2.copy()
lst3.insert(1, '2a')
