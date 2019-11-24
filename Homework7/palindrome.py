"""
Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition.
Unittest coverage - 100%
"""


def check_palindrome(string):
    div = 1
    try:
        number = int(string)
    except ValueError as error:
        print("Error", error)
        return
    while number / div >= 10:
        div *= 10

    while number != 0:
        left = number // div
        right = number % 10

        if left != right:
            return False

        number %= div
        number //= div
        div = div / 100

    return True


check_palindrome("1234312")
check_palindrome("123454321")
check_palindrome("asdsa")
