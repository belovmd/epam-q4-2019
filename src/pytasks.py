# This is our module with functions:
# 1 generate_numbers
# 2 count_characters
# 3 fizzbuzz
# 4 is_palindrome


def generate_numbers(n=20):
    """generate dictionary {number: square of a number}"""
    dict3_1 = {i + 1: pow(i + 1, 2) for i in range(n)}
    res_string = str(dict3_1)
    return res_string


def count_characters(count_me='abcdefg'):
    """count the number of characters in the string (case non-sensitive)"""
    dict3_2 = {}
    for let in count_me.lower():
        if let in dict3_2:
            dict3_2[let] += 1
        else:
            dict3_2[let] = 1
    res_string = str(dict3_2)
    return res_string


def fizzbuzz(n=20):
    """Fizzbuzz функция"""
    number = 1
    output_list = []
    while number <= n:
        if (number % 15) == 0:
            output_list.append('FizzBuzz')
        elif (number % 3) == 0:
            output_list.append('Fizz')
        elif (number % 5) == 0:
            output_list.append('Buzz')
        else:
            output_list.append(number)
        number += 1
    return output_list


def is_palindrome(input_number=1):
    """Проверка числа на палиндром"""
    original_num = input_number
    ostatok = 0
    reversd_num = 0
    result = True
    while input_number != 0:
        ostatok = input_number % 10
        reversd_num = reversd_num * 10 + ostatok
        input_number = input_number // 10
    if original_num == reversd_num:
        result = True
    else:
        result = False
    return result
