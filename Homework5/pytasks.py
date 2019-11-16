def count_characters(count_me_string='abcc'):
    chars_counter = {}
    for i in count_me_string:
        chars_counter[i] = chars_counter.get(i, 0) + 1
    return chars_counter


def generate_numbers(n=20):
    return {i: i ** 2 for i in range(1, n + 1)}


def is_palindrome(number=313):
    number_length = len(str(number))
    for i in range(number_length, number_length // 2 - 1, -2):
        start_digit = number // 10 ** (i - 1)
        end_digit = number % 10
        if start_digit != end_digit:
            return False
        number = number % 10 ** (i - 1) // 10
    return True


def fizzbuzz(max_number=15):
    result_list = []
    for i in range(1, max_number + 1):
        if i % 15 == 0:
            result_list.append('FizzBuzz')
        elif i % 3 == 0:
            result_list.append('Fizz')
        elif i % 5 == 0:
            result_list.append('Buzz')
        else:
            result_list.append(i)
    return(result_list)
