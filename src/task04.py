"""
Subtask 1.
Implement the function unique_in_order which takes as argument a sequence
and returns a list of items without any elements with the same value
next to each other and preserving the original order of elements.
"""


def unique_in_order(iterable):
    if not iterable:
        return []

    rez = []
    curr = iterable[0]
    rez.append(curr)
    for it in iterable:
        if(it == curr):
            continue
        rez.append(it)
        curr = it

    return rez


"""
Subtask2:
to square every digit of a number.
For example, if we run 9119 through the function, 811181 will come out,
because 9**2 is 81 and 1**2 is 1.
"""


def square_digits(num):
    stringRepresentation = str(num)
    rezstring = ""
    for char in stringRepresentation:
        currentDigit = int(char)
        rezstring += str(currentDigit ** 2)

    return int(rezstring)


"""
Subtask3:
A digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n.
If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers.
"""


def digital_root(number):
    while number > 9:
        digitsSum = 0
        for digit in str(number):
            digitsSum += int(digit)
        number = digitsSum

    return number
