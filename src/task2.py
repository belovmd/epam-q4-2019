'''Palindrom'''


def palinrom(num):
    power = len(str(num)) - 1
    for i in range(1, (len(str(num)) // 2) + 1):
        first_digit = num // 10 ** power
        second_digit = num % 10
        if first_digit != second_digit:
            return False
        else:
            num = (num - first_digit * 10 ** power) // 10
            power -= 2
    return True


if __name__ == '__main__':
    print(palidrom(11112))
