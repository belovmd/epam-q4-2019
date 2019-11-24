"""Add a try-except statement to the body of this function
which handles a possible IndexError, which could occur if
the index provided exceeds the length of the list. Print
an error message if this happens:
"""


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as error:
        print('Error:' + str(error))


if __name__ == '__main__':
    print_list_element(thelist=[1, 2, 3], index=0)
    print_list_element(thelist=[1, 2, 3], index=6)
