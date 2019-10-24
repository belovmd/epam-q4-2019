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
    s = str(num)
    rezs = ""
    for c in s:
        v = int(c)
        rezs += str(v ** 2)

    return int(rezs)


"""
Subtask3:
A digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n.
If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers.
"""


def num2collection(num) -> list:
    rez = []

    while num:
        rez.append(num % 10)
        num //= 10

    return rez


def digital_root(n):
    s = sum(num2collection(n))

    while len(str(s)) > 1:
        n = s
        s = sum(num2collection(n))
    return s
