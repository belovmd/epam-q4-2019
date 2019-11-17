"""Write two modules pytasks.py and runner.py.

Module pytasks contains definition for functions from previous tasks.
Separate module runner contains runner() function.
runner module can be imported or started from command line as script.
runner() function can be called as:
runner() – all functions will be called with default values and result printed
to screen
runner(‘generate_numbers’) – print result  only for generate_numbers()
runner(‘generate_numbers’, ‘happy_numbers’) – print results for
generate_numbers() and  happy_numbers(). Any combination of functions can be
specified.
"""


def generate_numbers(n=20):
    """Function returns dictionary.

    The keys are numbers between 1 and n (both included) and the values
    are square of keys. n – function argument. Default is 20.
    """
    print({num: num ** 2 for num in range(1, n + 1)})


def count_characters(s='Eyjafjallajökull'):
    """Function count and return the numbers of each character in a string.

    Default is "Eyjafjallajökull".
    """
    dct = {}
    for symb in s:
        dct[symb] = dct.get(symb, 0) + 1
    print(dct)


def is_palindrome(string_of_numbers='12345678987654321'):
    """Program checks whether a number is palindrome (True) or not (False).

    Default is "12345678987654321".
    """
    number = int(string_of_numbers)
    a = number
    palindrome = 0
    while number:
        res = number % 10
        palindrome = palindrome * 10 + res
        number //= 10
    if a == palindrome:
        print(True)
    else:
        print(False)


def fiz_buzz(num=101):
    """Program returns list of numbers from 1 to "num".

    For multiples of three prints “Fizz” instead of the number. For multiples
    of five prints “Buzz”. For numbers which are multiples of both three and
    five prints “FizzBuzz”. Default is 101.
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
    print(result_list)


if __name__ == '__main__':
    fiz_buzz()
    is_palindrome()
    count_characters()
    generate_numbers()
