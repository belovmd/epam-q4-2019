"""Get a tuple and return a tuple with 3 elements.

Pick the first, third and second to the last for the given array."""


def easy_unpack(elements: tuple) -> tuple:
    return elements[0], elements[2], elements[-2]


print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
