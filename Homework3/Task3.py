# Use a list comprehension to construct the list
# # ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

list_1 = [i + j for i in 'ab' for j in 'bcd']

# Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].

list_2 = list_1[::2]

# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].

list_3 = [i + 'a' for i in '1234']

# Simultaneously remove the element '2a' from the above list and print it.

print(list_3.pop(1))

# Copy the above list and add '2a' back into the list such that the
# original is still missing it.

copied_list = list_3.copy()
copied_list.insert(1, '2a')


# Create the list ['a', 'b', 'c'], then create a tuple from that list.

list_1t = ['a', 'b', 'c']
tuple_1 = tuple(list_1t)

# Create the tuple ('a', 'b', 'c'), then create a list from that tuple.

tuple_2 = ('a', 'b', 'c')
list_2t = list(tuple_2)

# Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
# (That is, in one line of code).

a, b, c = 'a', 2, 'gamma'

# Create a tuple containing just a single element which in turn contains the
# three elements 'a', 'b', and 'c'. Verify that the length is actually 1 by
# using the len() function.

tuple_3 = (('a', 'b', 'c'),)
print(len(tuple_3))


def generate_numbers(n=20):
    """returns a dictionary where the keys are numbers between 1 and n
    (both included) and the values are square of keys
    """

    return {i: i ** 2 for i in range(1, n + 1)}


def count_characters(count_me_string):
    """count and return the numbers of each character in a
    count_me_string argument
    """

    chars_counter = {}
    for i in count_me_string:
        chars_counter[i] = chars_counter.get(i, 0) + 1
    return chars_counter


def test1(a):

    """count and return the numbers of each character
    in a count_me_string argument"""

    return a


def test2(a):

    """count and return the numbers of each character
    in a count_me_string argument"""
    return a


def test3(a):

    """count and return the numbers of each character
    in a count_me_string argument
    """
    return a


def test4(a):

    """count and return the numbers of each character
    in a count_me_string argument
    """

    return a


def test5(a):

    """
    count and return the numbers of each character
    in a count_me_string argument"""

    return a


def test6(a):

    """
    count and return the numbers of each character
    in a count_me_string argument"""
    return a


def test7(a):

    """
    count and return the numbers of each character
    in a count_me_string argument
    """
    return a


def test8(a):

    """
    count and return the numbers of each character
    in a count_me_string argument
    """

    return a


def test9(a):
    """count and return the numbers of each character
    in a count_me_string argument"""

    return a


def test10(a):
    """count and return the numbers of each character
    in a count_me_string argument"""
    return a


def test11(a):
    """count and return the numbers of each character
    in a count_me_string argument
    """
    return a


def test12(a):
    """count and return the numbers of each character
    in a count_me_string argument
    """

    return a


def test13(a):
    """
    count and return the numbers of each character
    in a count_me_string argument"""

    return a


def test14(a):
    """
    count and return the numbers of each character
    in a count_me_string argument"""
    return a


def test15(a):
    """
    count and return the numbers of each character
    in a count_me_string argument
    """
    return a


def test16(a):
    """
    count and return the numbers of each character
    in a count_me_string argument
    """

    return a
