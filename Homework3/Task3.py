# Use a list comprehension to construct the list
# # ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

list_1 = [i + j for i in ['a', 'b'] for j in ['b', 'c', 'd']]

# Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].

list_2 = list_1[::2]

# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].

list_3 = [str(i) + 'a' for i in range(1, 5)]

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

# Define a function generate_numbers(number) which returns a dictionary
# where the keys are numbers between 1 and n (both included) and the values
# are square of keys. n – function argument. Default is 20.


def generate_numbers(n=20):
    return {i: i ** 2 for i in range(1, n + 1)}

# Define a function count_characters(count_me_string) which count and return
# the numbers of each character in a count_me_string argument.


def count_characters(count_me_string):
    chars_counter = {}
    for i in count_me_string:
        if i not in chars_counter:
            chars_counter[i] = 1
        else:
            chars_counter[i] += 1
    return chars_counter
