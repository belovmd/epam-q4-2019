num = input("Please enter the number:")
length = len(num)
number = int(num)
while length > 1:
    first_digit, number = divmod(number, 10 ** (length - 1))
    number, last_digit = divmod(number, 10)
    if first_digit != last_digit:
        print("Ordinary")
        break
    length -= 2
else:
    print("Palindrome")
