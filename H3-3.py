'''
Dictionary practice
'''


# Define a function generate_numbers(number)
# which returns a dictionary where the keys are numbers
# between 1 and n (both included) and the values are square
# of keys. n – function argument. Default is 20.
def generate_numbers(number):
    return dict((i, i ** 2) for i in range(number))


# Define a function count_characters(count_me_string)
# which count and return the numbers
# of each character in a count_me_string argument.
def count_characters(count_me_string):
    return {i: count_me_string.count(i) for i in count_me_string}


print(generate_numbers(20))
print(count_characters("abcdefcbac"))