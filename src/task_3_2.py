"""Tuple practice."""

# Create the list ['a', 'b', 'c'], then create a tuple from that list.

list_1 = ['a', 'b', 'c']
TUPLE_1 = tuple(list_1)


# Create the tuple ('a', 'b', 'c'), then create a list from that tuple.

list_1 = list(TUPLE_1)


# Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
# (That is, in one line of code).

a, b, c = "a", 2, "gamma"


# Create a tuple containing just a single element which in turn contains
# the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.

TUPLE_1_IN_TUPLE = (TUPLE_1,)

print(len(TUPLE_1_IN_TUPLE))
