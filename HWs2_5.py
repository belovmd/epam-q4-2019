# -*- coding: utf-8 -*-

def finding_palindrome():
    """finding_palindrome

    Check whether a number is palindrome or Not.
    Number must be string contains only numbers.
    """

    number = int(input("Enter number to palindrome test: "))
    number_copy = number
    inverted_number = 0

    while number >= 1:
        inverted_number = inverted_number * 10 + (number % 10)
        number = number // 10

    return True if inverted_number == number_copy else False


def fizzbuzz():
    """FizzBuzz

    Program prints the numbers from 1 to 100, but for multiples of
    three print “Fizz” instead of the number and for multiples of five print
    Buzz. For numbers which are multiples of both three and five,
    print “FizzBuzz”.
    """

    lst = []
    for number in range(1, 101):
        if number % 15 == 0:
            lst += ["FizzBuzz"]
        elif number % 3 == 0:
            lst += ["Fizz"]
        elif number % 5 == 0:
            lst += ["Buzz"]
        else:
            lst += [number]
    return lst


def generate_numbers(number=20):
    return {key: key ** 2 for key in range(1, number + 1)}


def count_characters():
    count_me_string = input("Enter string to count characters: ")
    letters_dict = {}
    for lett in count_me_string:
        letters_dict[lett] = letters_dict.get(lett, 0) + 1
    return letters_dict
