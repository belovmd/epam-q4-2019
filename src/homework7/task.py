"""Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition."""


def is_palindrome(number):
    if not isinstance(number, int):
        raise ValueError()

    if number < 0:
        return False

    original_number = number
    reversed_number = 0

    while number:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10

    return original_number == reversed_number
