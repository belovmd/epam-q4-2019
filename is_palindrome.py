number = int(input('input number: '))
a = number
pal = 0
while number:
    res = number % 10
    pal = pal * 10 + res
    number //= 10
if a == pal:
    print(a, 'is palindrome.')
else:
    print(a, 'is not palindrome.')
