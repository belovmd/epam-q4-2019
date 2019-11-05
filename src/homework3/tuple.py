"""Practice with tuples"""

# Create the list ['a', 'b', 'c'], then create a tuple from that list.
list1 = ["a", "b", "c"]
tuple1 = tuple(list1)
print(list1, tuple1)

# Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
# (Hint: the material needed to do this has been covered,
# but it's not entirely obvious)
tuple2 = "a", "b", "c"
list2 = list(tuple2)
print(list2, tuple2)

# Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
# (That is, in one line of code).
a, b, c = "a", 2, "gamma"

# Create a tuple containing just a single element which in turn contains
# the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.
tuple3 = tuple2,
print(tuple3, len(tuple3))
