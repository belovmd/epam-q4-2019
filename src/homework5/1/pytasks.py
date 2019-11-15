

# Define a function generate_numbers(number) which returns a dictionary
# where the keys are numbers between 1 and n (both included) and the values
# are square of keys. n – function argument. Default is 20.
def generate_numbers(n=20):
    return dict([(i, i * i) for i in range(1, n + 1)])


# Define a function count_characters(count_me_string) which count and return
# the numbers of each character in a count_me_string argument.
# Example:
# If the following string is given as argument to the function:
# abcdefgabc
# Then, the return result of the function should be:
# {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
def count_characters(count_me_string="abcdefgabc"):
    dct = {}
    for ltr in count_me_string:
        dct[ltr] = dct.get(ltr, 0) + 1
    return dct


# Write a program that prints the numbers from 1 to 100, but for multiples
# of three print “Fizz” instead of the number and for multiples of five
# print “Buzz”. For numbers which are multiples of both three and five,
# print “FizzBuzz”.
def fizzbuzz():
    number_list = []
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            number_list.append("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0))
        else:
            number_list.append(i)
    return number_list


# Write a program that check whether a number is palindrome or Not. Input
# string contains only numbers. Please work only arithmetic operations,
# loops and if-condition.
def is_palindrome(num="123456789087654321"):
    length = len(num)
    number = int(num)
    while length > 1:
        first_digit, number = divmod(number, 10 ** (length - 1))
        number, last_digit = divmod(number, 10)
        if first_digit != last_digit:
            return False
        length -= 2
    else:
        return True
