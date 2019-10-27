import math

# 2 functions searching for a palindrome:
# 1st is working with int input
# 2nd - with strings from wiki (as mentioned in the homework requirements)
# try - except construction assigns input to an appropriate function
# and prepares the strings for strpalindrome() function


def intpalindrome(a):
    length = int(math.log10(a)) + 1
    i = 0
    listing1 = []
    while i != length:
        x = a // (10 ** i) % 10
        listing1.append(x)
        i += 1
    listing2 = listing1[::-1]
    if listing2 == listing1:
        print('YES, it is an int palindrome!')
    else:
        print('NO, it is not a palindrome!')


def strpalindrome(a):
    x = ''
    for i in a:
        x = i + x
        if a == x:
            print('YES, it is a str palindrome!')


input_var = input()

try:
    input_var = int(input_var)
    intpalindrome(input_var)
except Exception:
    input_var = input_var.replace(' ', '')
    input_var = input_var.replace(',', '')
    input_var = input_var.replace('–', '')
    input_var = input_var.replace('\'', '')
    input_var = input_var.lower()
    print(input_var)
    strpalindrome(input_var)
