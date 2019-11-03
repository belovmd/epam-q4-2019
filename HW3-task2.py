"""Tuple practice
1. Create the list ['a', 'b', 'c'], then create a tuple from that list.
2. Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
(Hint: the material needed to do this has been covered, but it's not entirely
obvious)
3. Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
(That is, in one line of code).
4. Create a tuple containing just a single element which in turn contains the
three elements 'a', 'b', and 'c'. Verify that the length is actually 1 by
using the len() function.
"""
lst1 = ['a', 'b', 'c']
tuple1 = (tuple(lst1))

tuple2 = ('a', 'b', 'c')
lst2_1 = list(tuple2)  # way1
lst2_2 = [i for i in tuple2]  # way2, using generators

a, b, c = 'a', 2, 'gamma'

tuple4 = ([1, 2, 3], )
print(len(tuple4) == 1)
