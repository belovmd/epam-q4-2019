def print_list_element(thelist, index):
    """Handle Index exception."""

    try:
        print(thelist[index])
    except IndexError:
        print("Exception: "
              "index exceedes length of the list")


z = [1, 2, 3]
print_list_element(z, 22)
