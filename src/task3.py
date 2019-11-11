"""Dictionary practice

1. Define a function generate_numbers(number) which returns a dictionary
    where the keys are numbers between 1 and n (both included)
    and the values are square of keys. n – function argument.
    Default is 20.
2. Define a function count_characters(count_me_string)
    which count and return the numbers of each character
    in a count_me_string argument.
Example:
If the following string is given as argument to the function:
abcdefgabc
Then, the return result of the function should be:
{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
"""


# 1
def generate_numbers(num=20):
    return {el: el**2 for el in range(num + 1)}


# 2
def count_characters(count_me_string):
    return {
        char: count_me_string.count(char)
        for char in sorted(set(count_me_string))
    }
