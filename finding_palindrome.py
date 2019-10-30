"""
Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition
"""

number = abs(int(input()))

original_number = number
reversed_number = 0

while number:
    reversed_number = reversed_number * 10 + number % 10
    number //= 10

if original_number == reversed_number:
    print("It is palindrome")
else:
    print("It is not palindrome")
