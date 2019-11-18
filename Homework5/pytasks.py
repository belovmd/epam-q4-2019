def generate_numbers(n=20):
    """Returns dict (i: i^2)"""
    return {key: key ** 2 for key in range(1, n + 1)}


def count_characters(str1="aabcbdcbbabcbabc"):
    """Returns the numbers of each character in a count_me_string argument"""
    dct = {elem: str1.count(elem) for elem in str1}
    return dct


def fizzbuzz():
    """Returns list of values"""
    lst = []
    for number in range(1, 101):
        if (number % 3 == 0) or (number % 5 == 0):
            lst.append("Fizz" * (not number % 3) + "Buzz" * (not number % 5))
        else:
            lst.append(number)
    return lst


def is_palindrome(number=12321):
    """Returns True or False"""
    div = 1
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
