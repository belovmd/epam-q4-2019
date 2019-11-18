"""Determine if given number is palindrome."""


def is_palindrome(number=12321):
    buff = number
    reversed = 0

    while buff:
        reversed *= 10
        reversed += buff % 10
        buff //= 10

    result = reversed == number
    print("is {} palindrome?: {}".format(number, result))
    return result


"""Classic fizz buzz task
Print Fizz if number devided by 3,
Buzz if number devided by 5,
FizzBuzz if number devided by 3 and by 5.
"""


def fizzbuzz(max_number=20):
    formatlist = ['', 'Fizz', 'Buzz', 'FizzBuzz']
    result = []

    for num in range(1, max_number):
        formatlist[0] = num
        result.append('{}'.format(
            formatlist[(num % 3 == 0) + 2 * (num % 5 == 0)]))

    print("\n".join(result))


"""generate_numbers

    Define a function generate_numbers(number) which returns a dictionary
    where the keys are numbers between 1 and n (both included)
    and the values are square of keys. n – function argument.
    Default is 20."""


def generate_numbers(num=20):
    result = {el: el**2 for el in range(num + 1)}

    print(result)


"""count_characters

Define a function count_characters(count_me_string)
which count and return the numbers of each character
in a count_me_string argument.
Example:
If the following string is given as argument to the function:
abcdefgabc
Then, the return result of the function should be:
{'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
"""


def count_characters(count_me_string='abcdefgabc'):
    result = {
        char: count_me_string.count(char)
        for char in sorted(set(count_me_string))
    }

    print(result)
