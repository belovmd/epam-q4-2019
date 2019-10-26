def palindrome(number):
    reverse = 0
    copy_number = number
    while copy_number:
        reverse *= 10
        reverse += copy_number % 10
        copy_number = copy_number // 10

    if number == reverse:
        return True
    else:
        return False


if __name__ == '__main__':
    num = int(input('Please enter the number '))
    if palindrome(num):
        print('This number is palindrome')
    else:
        print('This number is not palindrome')
