# 2.1 create tuple from list
list_1 = ['a', 'b', 'c']
tuple_1 = tuple(list_1)
assert isinstance(tuple_1, tuple)
print(tuple_1)

# 2.2 create list from tuple
tuple_2 = ('a', 'b', 'c')
list_2 = list(tuple_2)
assert isinstance(list_2, list)
print(list_2)

# 2.3 Assign variable simultaneously
a, b, c = 'a', 2, 'gamma'
assert a == 'a'
assert b == 2
assert c == 'gamma'
print(a, b, c)

# 2.4 Create a tuple of tuples
tuple_3 = (('a', 'b', 'c'), )
assert len(tuple_3) == 1
print(len(tuple_3))
