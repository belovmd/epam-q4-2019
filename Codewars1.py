''' In this kata you will create a function
that takes a list of non-negative integers
and strings and returns a new list with the
strings filtered out.'''


def filter_list(l):
    i = 0
    while i != len(l):
        if type(l[i]) != int:
            l.pop(i)
        else:
            i += 1
            continue
    return l


'''An isogram is a word that has no repeating letters,
consecutive or non-consecutive. Implement a function
that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.'''


def is_isogram(string):
    string = string.lower()
    listing = []
    i = 0
    if string == '':
        return True
    while i != len(string):
        if listing.count(string[i]) != 0:
            return False
            break
        elif len(listing) + 1 == len(string):
            return True
        else:
            listing.append(string[i])
            i += 1


''' Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci,
but summing the last 3 (instead of 2) numbers of the sequence to
generate the next. And, worse part of it, regrettably I won't get
to hear non-native Italian speakers trying to pronounce it :('''


def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        listing = []
        listing.append(signature[0])
        return listing
    elif n == 2:
        listing = []
        listing.append(signature[0])
        listing.append(signature[1])
        return listing
    i = 2
    while n - 1 != i:
        y = signature[i] + signature[i - 1] + signature[i - 2]
        signature.append(y)
        i += 1
        print(signature)
    return signature
