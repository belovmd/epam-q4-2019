""" Tuple practice"""

# Create  the list ['a', 'b', 'c'], then create tuple from this list
list_1 = ['a', 'b', 'c']
tuple_1 = tuple(list_1)
print('{0}\n{1}'.format(list_1, tuple_1))

# create  the tuple ('a', 'b', 'c'), then create list from this tuple
tuple_2 = ('a', 'b', 'c')
list_2 = list(tuple_2)
print('{0} \n{1}'.format(tuple_2, list_2))

# a = 'a', b = 2, c = 'gamma' in one line
a, b, c = 'a', 2, 'gamma'
print('a = {0}, \nb = {1} \nc = {2}'.format(a, b, c))

# Create a tuple containing just a single element  which in turn contains
# three elements 'a', 'b', 'v'
tuple_3 = (tuple_2,)
print('tuple: {0} \nlength = {1}'.format(tuple_3, len(tuple_3)))
