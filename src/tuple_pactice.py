""" Tuple practice"""

# Create  the list ['a', 'b', 'c'], then create tuple from this list
list_1 = ['a', 'b', 'c']
tuple_1 = tuple(list_1)
print(f'{list_1}\n{tuple_1}')

# create  the tuple ('a', 'b', 'c'), then create list from this tuple
tuple_2 = ('a', 'b', 'c')
list_2 = list(tuple_2)
print(f'{tuple_2} \n{list_2}')

# a = 'a', b = 2, c = 'gamma' in one line
a, b, c = 'a', 2, 'gamma'
print(f'a = {a}, \nb = {b} \nc = {c}')

# Create a tuple containing just a single element  which in turn contains three elements 'a', 'b', 'v'
tuple_3 = (tuple_2,)
print(f'tuple: {tuple_3} \nlength = {len(tuple_3)}')
