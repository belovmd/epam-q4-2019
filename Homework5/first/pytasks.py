"""
Functions from another tasks
"""


def generate_numbers(n=20):
    return {number: number ** 2 for number in range(1, n + 1)}


def count_characters(count_me_string='auvsdafasd'):
    count = {}
    for symbol in count_me_string:
        count[symbol] = count.setdefault(symbol, 0) + 1
    return count


def fizz_buzz():
    lst = []
    for number in range(1, 101):
        if number % 3 == 0 or number % 5 == 0:
            lst.append("Fizz" * (number % 3 == 0) + "Buzz" * (number % 5 == 0))
        else:
            lst.append(number)
    return lst


def palindrome(number=123321):
    reverse = 0
    copy_number = number
    while copy_number:
        reverse *= 10
        reverse += copy_number % 10
        copy_number = copy_number // 10

    return number == reverse
