#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 05 1
Sergey Streltsov 2019-11-17
pytasks module, countains functions from homework02
"""


def fizzbuzz():
    """EPAM python q4 homework 02.3 FizzBuzz

    Write a program that prints the numbers from 1 to 100,
    but for multiples of three print “Fizz” instead of the number
    and for multiples of five print “Buzz”.
    For numbers which are multiples of both three and five, print “FizzBuzz”.
    ( http://en.wikipedia.org/wiki/Biz... )
    """
    fizz_buzz_values = list()
    for number in range(1, 101):
        if number % 15 == 0:
            fizz_buzz_values.append('FizzBuzz')
        elif number % 3 == 0:
            fizz_buzz_values.append('Fizz')
        elif number % 5 == 0:
            fizz_buzz_values.append('Buzz')
        else:
            fizz_buzz_values.append(number)
    return fizz_buzz_values


def is_palindrome(input_str='7890987'):
    """EPAM python q4 homework 02.1 Finding palindrome v3

    Write a program that check whether a number is palindrome or Not.
    Input string contains only numbers.
    Please work only arithmetic operations, loops and if-condition.
    """
    if not input_str:
        input_str = input('Enter a number: ')
    try:
        num_value = value_copy = int(input_str)
        new_value = 0
        while num_value:
            remain = num_value % 10
            new_value = new_value * 10 + remain
            num_value //= 10
        return value_copy == new_value
    except ValueError:
        print('Error, not a number')


def count_characters(count_me_string='myteststringfromprevioustask'):
    """Dictionary practice

    Define a function count_characters(count_me_string) which count and return
    the numbers of each character in a count_me_string argument.
    """
    counted = dict()
    for ch in count_me_string:
        counted[ch] = counted.get(ch, 0) + 1
    return counted


def generate_numbers(number=20):
    """Dictionary practice

    Define a function generate_numbers(number) which returns a dictionary
    where the keys are numbers between 1 and n (both included) and the values
    are square of keys. n – function argument. Default is 20.
    """
    return {n: n * n for n in range(1, number + 1)}
