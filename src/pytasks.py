""" Function from  previous tasks """


def fizzbuzz(range_=2):
    number_list = []
    for i in range(1, range_ + 1):
        if i % 3 == 0 or i % 5 == 0:
            number_list.append("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0))
        else:
            number_list.append(i)
    return number_list


def gen_numbers(numbers=3):
    return {digit: digit ** 2 for digit in range(1, numbers + 1)}


def palindrome(num=11):
    if type(num) == int:
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
    else:
        return 'Input must be a number'
