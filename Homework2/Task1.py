chosen_string = input('Write any string: ').lower()
reverse_string = chosen_string[::-1].lower()
if chosen_string and chosen_string == reverse_string:
    print('Palindrome')
else:
    print('Not palindrome')
