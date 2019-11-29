""" Add a try-except statement to the body
of this function which handles a possible IndexError,
which could occur if the index provided exceeds
the length of the list"""


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as err:
        print("KeyError")

print_list_element((1, 2, 3, 4, 5), 8)
