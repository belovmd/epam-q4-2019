"""Tuple practice."""

# Create the list ['a', 'b', 'c'], then create a tuple from that list.

practice_list = ['a', 'b', 'c']
PRACTICE_TUPLE = tuple(practice_list)


# Create the tuple ('a', 'b', 'c'), then create a list from that tuple.

practice_list = list(PRACTICE_TUPLE)


# Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
# (That is, in one line of code).

a, b, c = "a", 2, "gamma"  # requirements pylint: disable=C0103


# Create a tuple containing just a single element which in turn contains
# the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.

MAGIC_PRACTICE_TUPLE = PRACTICE_TUPLE,  # pylint: disable=R1707
# https://bugs.python.org/issue2817

print('Tuple lenth verified.' * bool(len(MAGIC_PRACTICE_TUPLE) == 1) or
      'Tuple length not verified.')
