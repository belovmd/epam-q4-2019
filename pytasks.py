def generate_numbers(n=20):
    return {key: key ** 2 for key in range(1, n + 1)}


def count_characters(count_me_string="abcdefgh"):
    result = {}
    for char in count_me_string:
        result[char] = result.get(char, 0) + 1
    return result


def is_palindrome(number=123321):
    original_number = number
    reversed_number = 0

    while number:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10

    return original_number == reversed_number


def fizz_buzz(start=1, num=100):
    result = []
    for i in range(start, num):
        if not i % 15:
            result.append("FizzBuzz")
        elif not i % 3:
            result.append("Fizz")
        elif not i % 5:
            result.append("Buzz")
        else:
            result.append(i)
    return result
