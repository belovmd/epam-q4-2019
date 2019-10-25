number = str(input('input number: '))
pos = 0
while pos < len(number) / 2:
    if number[0 + pos] == number[-1 -pos]:
        pos += 1
        continue
    else:
        print(number, 'is not palindrome.')
        break
else:
    print(number, 'is palindrome.')
