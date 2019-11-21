"""Add a try-except statement to the body of this function which handles a
possible IndexError, which could occur if the index provided exceeds the
length of the list. Print an error message if this happens."""


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as error:
        print(str(error))


my_list = list(elem for elem in range(1000) if not elem % 3)
print_list_element(my_list, 333)
print_list_element(my_list, 334)
