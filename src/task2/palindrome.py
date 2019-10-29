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
    print(f"{number_to_check} is a palindrome")
else:
    print(f"{number_to_check} is not a palindrome")
