""" Tuple practice """

# 1)Create the list ['a', 'b', 'c'], then create a tuple from that list.
lst = ['a', 'b', 'c']
tpl1 = tuple(lst)
print(tpl1)

# 2)Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
tpl2 = ('a', 'b', 'c')
lst2 = list(tpl2)
print(lst2)

# 3)Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
# (That is, in one line of code).
a, b, c = 'a', 2, 'gamma'
print(a, b, c)

# 4)Create a tuple containing just a single element which in turn contains
# the three elements 'a', 'b', and 'c'. Verify that the length is actually 1
# by using the len() function.
tpl3 = (('a', 'b', 'c',),)
print(len(tpl3))
