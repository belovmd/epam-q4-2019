"""Find palindrome

Check whether a number is palindrome or Not.
Input string contains only numbers.
"""


number_to_check = input("Enter a number: ")
reversed_number = ""
number_to_check_len = len(number_to_check)

while number_to_check_len:
    number_to_check_len -= 1
    reversed_number += number_to_check[number_to_check_len]

if reversed_number == number_to_check:
    print("{} is a palindrome".format(number_to_check))
else:
    print("{} is not a palindrome".format(number_to_check))
