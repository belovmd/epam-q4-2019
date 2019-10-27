""" Finding palindrome
Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition.
"""

number = int(input("Enter number: \n"))
if number:
    len_of_number = 0
    while True:
        if number >= 10 ** len_of_number:
            len_of_number += 1
        else:
            break
    is_palindrome = True
    for n in range(len_of_number // 2):
        if (number // (10 ** (len_of_number - n - 1))) % 10 != \
                (number // (10 ** n)) % 10:
            is_palindrome = False
            break
    print('It is a palindrome' if is_palindrome else 'It is not a palindrome')

else:
    print("Sorry, you enter empty number")
