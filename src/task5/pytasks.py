def generate_numbers(number=20):
    try:
        number = int(number)
    except Exception:
        raise Exception
    return {a: a ** 2 for a in range(number + 1) if a > 0}


def count_characters(count_me_string='foo'):
    try:
        count_me_string = str(count_me_string)
    except Exception:
        raise Exception
    if len(count_me_string) == 0:
        raise ValueError('Empty string input is not allowed')

    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890,.;'
    count_me_string = count_me_string.lower()
    return {letter: count_me_string.count(letter)
            for letter in alphabet
            if count_me_string.count(letter) > 0}


def fizzbuzz(input_number=15):
    for number in range(1, input_number):
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "FizzBuzz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return number


def is_palindrome(number_to_check='32'):
    if number_to_check is None:
        number_to_check = input("Enter a number: ")
    reversed_number = ""
    number_to_check_len = len(number_to_check)

    while number_to_check_len:
        number_to_check_len -= 1
        reversed_number += number_to_check[number_to_check_len]

    if reversed_number == number_to_check:
        return "{} is a palindrome".format(number_to_check)
    else:
        return "{} is not a palindrome".format(number_to_check)
