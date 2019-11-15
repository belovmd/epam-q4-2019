"""Dictionary practice."""

# Define a function generate_numbers(number) which returns a dictionary
# where the keys are numbers between 1 and n (both included) and the
# values are square of keys. n – function argument. Default is 20.


def generate_numbers(number=20):
    """generate_numbers.

    Return a dictionary where the keys are numbers
    between 1 and n (both included) and the values are
    square of keys. n – function argument. Default is 20.
    """
    square_num_dict = {}
    for index in range(1, number + 1):
        square_num_dict[index] = index * index

    return square_num_dict


#  Define a function count_characters(count_me_string) which count and
#  return the numbers of each character in a count_me_string argument.


def count_characters(count_me_string):
    """Count frequences of all characters in string.

    Argument:

    count_me_string - string for counting frequences of
    characters

    Example:
    count_characters('abcdefgabc')

    {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}

    """
    freq_of_chars = {}
    for character in count_me_string:
        freq_of_chars[character] = freq_of_chars.get(character, 0) + 1
    return freq_of_chars
