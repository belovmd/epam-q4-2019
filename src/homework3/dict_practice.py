""" Dictionary practice """


# Define a function generate_numbers(number) which returns a dictionary
# where the keys are numbers between 1 and n (both included)
# and the values are square of keys. n – function argument. Default is 20.
def generate_numbers(n=20):
    return dict((key, key * key) for key in range(1, n + 1))


# Define a function count_characters(count_me_string) which count and
# return the numbers of each character in a count_me_string argument.
def count_characters(count_me_string):
    result = {}
    for char in count_me_string:
        result.setdefault(char, 0)
        result[char] += 1
    return result
