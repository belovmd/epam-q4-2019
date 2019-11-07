# 1. Create the list ['a', 'b', 'c'], then create a tuple from that list
lst1 = list('abc')
tup1 = tuple(lst1)

# 2. Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
tup2 = tuple('abc')
lst2 = list(tup2)

# 3. Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
a, b, c = 'a', 2, 'gamma'

# 4. Create a tuple containing just a single element which in turn contains the
# three elements 'a', 'b', and 'c'. Verify that the length is actually 1 by
# using the len() function.
tup3 = (['a', 'b', 'c'], )
print(len(tup3))
