""" Dictionary practice """


# Define a function generate_numbers(number)
# which returns a dictionary where the keys
# are numbers between 1 and n (both included)
# and the values are square of keys. n – function argument. Default is 20.
def generate_numbers(n=20):
    return {number: number ** 2 for number in range(1, n + 1)}


# Define a function count_characters(count_me_string)
# which count and return the numbers of each character
# in a count_me_string argument.
def count_characters(count_me_string):
    return {sym: count_me_string.count(sym) for sym in count_me_string}


print(generate_numbers(20))
print(count_characters("abcdefgabc"))
