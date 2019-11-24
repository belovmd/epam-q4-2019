"""Add a try-except statement to the body of this function which handles a
possible IndexError, which could occur if the index provided exceeds the
length of the list. Print an error message if this happens.
"""


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print('Index provided exceeds the length of the list.')


lst = [1, 2, 3, 4, 'e', 'wwww', 345]
print_list_element(lst, 15)
print_list_element(lst, 3)
