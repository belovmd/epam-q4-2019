def generate_numbers(n=20):
    """Function returns dictionary.

    The keys are numbers between 1 and n (both included) and the values
    are square of keys. n – function argument. Default is 20.
    """
    return {num: num ** 2 for num in range(1, n + 1)}


def count_characters(s):
    """Function count and return the numbers of each character in a string."""
    dct = {}
    for symb in s:
        dct[symb] = dct.get(symb, 0) + 1
    return dct


def is_palindrome(string_of_numbers):
    """Program checks whether a number is palindrome (True) or not (False)"""
    number = int(string_of_numbers)
    a = number
    palindrome = 0
    while number:
        res = number % 10
        palindrome = palindrome * 10 + res
        number //= 10
    if a == palindrome:
        return True
    else:
        return False


def fiz_buzz(num):
    """Program returns list of numbers from 1 to "num".

    For multiples of three prints “Fizz” instead of the number. For multiples
    of five prints “Buzz”. For numbers which are multiples of both three and
    five prints “FizzBuzz”.
    """
    result_list = []
    for number in range(num):
        if number % 15 == 0:
            result_list.append('FizzBuzz')
        elif number % 3 == 0:
            result_list.append('Fizz')
        elif number % 5 == 0:
            result_list.append('Buzz')
        else:
            result_list.append(number)
    return result_list
