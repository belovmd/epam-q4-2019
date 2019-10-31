""" Finding palindrome
Write a program that check whether a number is palindrome or Not.
Input string contains only numbers.
Please work only arithmetic operations, loops and if-condition.
"""

number = int(input("Enter number: \n"))
number_copy = number
inverted_number = 0

while number >= 1:
    inverted_number = inverted_number * 10 + (number % 10)
    number = number // 10

print("Palindrome" if inverted_number == number_copy else "Not palindrome")
