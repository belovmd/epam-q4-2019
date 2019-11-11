"""Tuple practice

1. Create the list ['a', 'b', 'c'], then create a tuple from that list.
2. Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
    (Hint: the material needed to do this has been covered,
    but it's not entirely obvious)
3. Make the following instantiations simultaneously:
    a = 'a', b=2, c='gamma'. (That is, in one line of code).
4. Create a tuple containing just a single element
    which in turn contains the three elements 'a', 'b', and 'c'.
    Verify that the length is actually 1 by using the len() function.
"""

# 1
lst = ['a', 'b', 'c']
tpl = tuple(lst)

# 2
tpl = ('a', 'b', 'c')
lst = list(tpl)

# 3
a, b, c = ('a', 2, 'gamma')
print("{}; {}; {}\n".format(a, b, c))

# 4
tpl = (('a', 'b', 'c'), )
print("tuple length: {}".format(len(tpl)))
