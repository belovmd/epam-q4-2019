"""
Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition
"""

number = input()
len_number = len(number)
number = int(number)

palindrome = True
for left in range(len_number - 1, 0, -2):
    if number % 10 != number // 10 ** left:
        palindrome = False
        break
    number %= 10 ** left
    number //= 10

if palindrome:
    print("It is palindrome")
else:
    print("It is not palindrome")
