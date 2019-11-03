"""
Dictionary practice

1. Define a function generate_numbers(number) which returns a dictionary where
the keys are numbers between 1 and n (both included) and the values are square
of keys. n – function argument. Default is 20.
2. Define a function count_characters(count_me_string) which count and return
the numbers of each character in a count_me_string argument.
Example:
If the following string is given as argument to the function:
abcdefgabc
Then, the return result of the function should be:
{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
"""


def generate_numbers(number=20):
    return {key: key ** 2 for key in range(1, number + 1)}


def count_characters(count_me_string):
    return {lett: count_me_string.count(lett) for lett in set(count_me_string)}
