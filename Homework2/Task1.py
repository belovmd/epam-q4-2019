''' Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition. '''

number = int(input('Write any int: '))
number_length = len(str(number))
for i in range(number_length, number_length // 2 - 1, -2):
    start_digit = number // 10 ** (i - 1)
    end_digit = number % 10
    if start_digit != end_digit:
        print('Not palindrome')
        break
    number = number % 10 ** (i - 1) // 10
else:
    print('Palindrome')
