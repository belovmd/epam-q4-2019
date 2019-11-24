"""Task 1.2

Add a try-except statement to the body of this function which handles a
possible IndexError, which could occur if the index provided exceeds the
length of the list. Print an error message if this happens:
"""


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as index_err:
        print(index_err)
