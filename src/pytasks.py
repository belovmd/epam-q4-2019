from collections import Counter


def fizzbuzz():
    range_ = int(input('fizzbuzz: Enter number'))
    number_list = []
    for i in range(1, range_ + 1):
        if i % 3 == 0 or i % 5 == 0:
            number_list.append("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0))
        else:
            number_list.append(i)
    return number_list


def count_characters():
    str_ = input('count_characters:Enter word')
    return dict(Counter(str_))


def gen_numbers():
    numbers = int(input('gen_number: Enter number'))
    return {digit: digit ** 2 for digit in range(1, numbers + 1)}


def palindrome():
    num = int(input('palindrome: Enter number'))
    power = len(str(num)) - 1
    for i in range(1, (len(str(num)) // 2) + 1):
        first_digit = num // 10 ** power
        second_digit = num % 10
        if first_digit != second_digit:
            return False
        else:
            num = (num - first_digit * 10 ** power) // 10
            power -= 2
    return True
