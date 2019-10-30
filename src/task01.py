"""Determine if given number is polynome."""


def isPoly(number):
    buff = number
    reversed = 0

    while buff:
        reversed *= 10
        reversed += buff % 10
        buff //= 10

    return reversed == number


num = int(input("Please, enter number to test\n"))
print(isPoly(num))
